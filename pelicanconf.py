#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eleftherios Garyfallidis'
SITENAME = u'Eleftherios Garyfallidis, PhD'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Dipy', 'http://dipy.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/Garyfallidis'),
          ('Facebook', 'https://www.facebook.com/garyfallidis'),
          ('Twitter', 'https://twitter.com/garyfallidis'),
          ('Google plus', 'https://plus.google.com/u/0/+EleftheriosGaryfallidis/posts'),)
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

TYPOGRIFY = True

#THEME = "/home/eleftherios/Devel/website-dev/themes/pelican-bootstrap3"
#THEME = "/home/eleftherios/Devel/website-dev/themes/pelican-bootstrap3-lovers"
THEME = "/home/eleftherios/Devel/website-dev/themes/eleftherios"


bs_theme_names = ["spacelab", "superhero", "cosmo", "cerulean", \
                  "cupid", "darkly", "flatly", "hiro", "journal", \
                  "lumen", "paper", "sandstone", "shamrock", \
                  "simplex", "slate", "united", "yeti"]
BOOTSTRAP_THEME = bs_theme_names[15]
print('Selected theme is ' + BOOTSTRAP_THEME)

#BOOTSTRAP_THEME = "amelia"
#BOOTSTRAP_THEME = "cyborg"


COPYRIGHT_YEAR = "2015" # COPYRIGHT YEAR
#CC_LICENSE = 'CC_BY'

#STATIC_PATHS = ['images']
#PROFILE_PICTURE = "profile.png"

