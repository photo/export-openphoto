Trovebox Export Tool
=======================
#### Trovebox, a photo service for the masses

----------------------------------------

<a name="overview"></a>
### Overview

This script fetches all of your photos from a Trovebox host
and stores them into text files which can then be easily imported into
another Trovebox host.

<a name="dependencies"></a>
### Getting dependencies

The only dependency you need is the `trovebox` module ([repository on Github](https://github.com/photo/openphoto-python)).

    sudo pip install trovebox

<a name="download"></a>
### Downloading the script

#### Using git

    git clone git://github.com/photo/export-openphoto.git

#### Using wget

    mkdir export-openphoto
    wget -O export-openphoto/fetch.py https://raw.github.com/photo/export-openphoto/master/fetch.py --no-check-certificate

#### Using file->save

Click the link below and save the file into a directory named `export-openphoto`.

https://raw.github.com/photo/export-openphoto/master/fetch.py

<a name="credentials"></a>
### Credentials

For full access to your photos, you need to create the following config file in ``~/.config/trovebox/default``

    # ~/.config/trovebox/default
    host = your.host.com
    consumerKey = your_consumer_key
    consumerSecret = your_consumer_secret
    token = your_access_token
    tokenSecret = your_access_token_secret

The ``--config`` commandline option lets you specify a different config file.

To get your credentials:
 * Log into your Trovebox site
 * Click the arrow on the top-right and select 'Settings'
 * Click the 'Create a new app' button
 * Click the 'View' link beside the newly created app

<a name="running"></a>
### Running the script

Start a terminal and enter the following.

    cd export-openphoto
    python fetch.py

Now the script gets to work downloading the information for your photos. It doesn't download the actual photos so it should be relatively fast.

    Parsing URL for the token... OK
    Fetching user id... OK
    Fetching page 1... OK
      * Storing photo 6109695003 to fetched/6109695003.json... OK
      * Storing photo 6109694841 to fetched/6109694841.json... OK
      * Storing photo 6109694637 to fetched/6109694637.json... OK
      * Storing photo 6110240318 to fetched/6110240318.json... OK
      * Storing photo 6110240222 to fetched/6110240222.json... OK
      * Storing photo 6065502023 to fetched/6065502023.json... OK
    Fetching page 2... OK

### YAY

Now you've got a bunch of text files. These can be fed into our [import tool](http://github.com/photo/import) to transfer all of your photos into your Trovebox account.

Don't worry, we'll have a nice web based GUI for all of this soon :).

