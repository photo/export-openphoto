#!/usr/bin/env python

import os
import json
import datetime
from trovebox import Trovebox

# Only the following fields will be exported:
EXPORT_FIELDS = ["dateTaken",
                 "dateUploaded",
                 "description",
                 "filenameOriginal",
                 "latitude",
                 "longitude",
                 "license",
                 "permission",
                 "rotation",
                 "status",
                 "tags",
                 "timestamp",
                 "title",
                 "views",
                 ]

# main program
def fetch(client):
  per_page = 100

  # we'll paginate through the results
  # start at `page` and get `per_page` results at a time
  page=1

  # store everything in a list or array or whatever python calls this
  photos_out=[]

  # while True loop till we get no photos back
  while True:
    # call the photos.list API
    # https://trovebox.com/documentation/api/GetPhotos
    print "Fetching page %d..." % page,
    photo_list = client.photos.list(pageSize=per_page, page=page)
    print "OK"

    # increment the page number before we forget so we don't endlessly loop
    page = page+1;

    # if the list of photos is empty we must have reached the end of this user's library and break out of the while True
    if len(photo_list) == 0:
      break;

    # else we loop through the photos
    for photo in photo_list:
      # get all the data we can
      p = {}
      fields = photo.get_fields()
      for field in fields:
        if field in EXPORT_FIELDS:
          p[field] = fields[field]

      p['photo'] = photo.pathOriginal

      t = datetime.datetime.fromtimestamp(float(photo.dateUploaded))
      filename = '%s-%s' % (t.strftime('%Y%m%dT%H%M%S'), photo.id)

      print "  * Storing photo %s to fetched/%s.json" % (photo.id, filename),
      f = open("fetched/%s.json" % filename, 'w')
      f.write(json.dumps(p))
      f.close()
      print "OK"

# create a directory only if it doesn't already exist
def createDirectorySafe( name ):
  if not os.path.exists(name):
    os.makedirs(name)

#################################################

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description="Backup your Trovebox photos")
  parser.add_argument('--config', help="Configuration file to use")
  parser.add_argument('--host', help="Hostname of the Trovebox server (overrides config_file)")
  parser.add_argument('--consumer-key')
  parser.add_argument('--consumer-secret')
  parser.add_argument('--token')
  parser.add_argument('--token-secret')
  parser.add_argument('--debug', help="Print extra debug information", action="store_true")
  config = parser.parse_args()

  if config.debug:
    logging.basicConfig(level=logging.DEBUG)

  # Host option overrides config file settings
  if config.host:
    client = Trovebox(host=config.host, consumer_key=config.consumer_key,
                      consumer_secret=config.consumer_secret,
                      token=config.token, token_secret=config.token_secret)
  else:
    try:
      client = Trovebox(config_file=config.config)
    except IOError as error:
      print error
      print
      print "You must create a configuration file in ~/.config/trovebox/default"
      print "with the following contents:"
      print "    host = your.host.com"
      print "    consumerKey = your_consumer_key"
      print "    consumerSecret = your_consumer_secret"
      print "    token = your_access_token"
      print "    tokenSecret = your_access_token_secret"
      print
      print "To get your credentials:"
      print " * Log into your Trovebox site"
      print " * Click the arrow on the top-right and select 'Settings'."
      print " * Click the 'Create a new app' button."
      print " * Click the 'View' link beside the newly created app."
      print
      print error
      sys.exit(1)

  # check if a fetched directory exist else create it
  createDirectorySafe('fetched')
  fetch(client)
