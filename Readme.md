# [WIP] 
`pip install git+https://github.com/felipecorrea/python-pocket` doesn't run ==> `pip install pocket` ([see project](https://github.com/tapanpandita/pocket)).

Need to adapt `get_access_token.py` for python 3 to get an access token (added in project). 

This change API and current project doesn't still run. Need some adaptation.

All with python 3.4.2


# Pocketmon

A script that tags my [Pocket](http://getpocket.com/) articles based on the time required to read them.

I thought of this some time ago, but then I found [readruler.com](http://readruler.com/) which basically does the same thing, but you have to open it everytime you add new articles, whereas this script can be just run as cron job :)

## Screenshots

![Tags on each article](screenshots/article_list.png)

![Tags list](screenshots/tag_list.png)

## Setup

<p>1. Install a wrapper to Pocket's API </p>

`pip install git+https://github.com/felipecorrea/python-pocket`

<p>2. Getting a consumer key.</p>

You can skip this step and just use the key of an application that I created: `44479-ea92cc886eed9b46660b84a4`

Or

Create a [new Pocket App](http://getpocket.com/developer/apps/new) & copy the consumer key of the application.

<p>3. Getting an access token</p>

```
$ git clone https://github.com/felipecorrea/python-pocket
$ python python-pocket/get_access_token.py
```

Enter your consumer key and allow access to the app in browser. This will print out your access token.

<p>4. Update the configuration</p>

`cp config.py.example config.py`

Store both the consumer key and access token in this new file.

<p>5. Test whether it works</p>

`$ python pocketmon.py`

It will tag all untagged articles.
