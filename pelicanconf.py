#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Martin'
SITENAME = 'Downright Dad'
SITEURL = ''
SITESUBTITLE = ''

PATH = 'content'


STATIC_PATHS = ['images', 'extra/custom.css']
CSS_OVERRIDE = ['extra/custom.css']


TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

THEME = 'themes/attila'
HEADER_COVER = 'images/finley.jpg'
HEADER_COLOR = 'black'

SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/myprofile'),
          ('facebook','https://facebook.com/myprofile'),
          ('flickr','https://www.flickr.com/myprofile/'),
          ('envelope','mailto:my@mail.address'))

GOOGLE_ANALYTICS = 'UA-118771828-3'


AUTHORS_BIO = {
  "martin": {
    "name": "Martin",
    "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "website": "https://martinnoah.com",
    "location": "New Jersey",
    "bio": "Daddy-o writing bloggy-o."
  }
}

