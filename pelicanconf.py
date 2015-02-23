#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eleftherios Garyfallidis'
SITENAME = u'Eleftherios Garyfallidis, PhD'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Dipy', 'http://dipy.org'), 
		 ('Nibabel', 'http://nipy.org/nibabel'),
		 ('Scholar Google', 'https://scholar.google.ca/citations?user=Ln2EyRYAAAAJ&hl=en'))

# Social widget
SOCIAL = (('Github', 'https://github.com/Garyfallidis'),
          ('Facebook', 'https://www.facebook.com/garyfallidis'),
          ('Twitter', 'https://twitter.com/garyfallidis'),
          ('Linkedin', 'https://www.linkedin.com/profile/view?id=17061033'),
          ('YouTube', 'https://www.youtube.com/user/Garyfallidis/videos'),
          ('Google plus', 'https://plus.google.com/u/0/+EleftheriosGaryfallidis/posts'),
          )
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
                  "simplex", "slate", "united", "yeti", \
                  "amelia", "cyborg"]
BOOTSTRAP_THEME = "hiro" #bs_theme_names[16]
print('>>> Selected theme is ' + BOOTSTRAP_THEME + '\n')

#BANNER = True
#BANNER_ALL_PAGES = True

COPYRIGHT_YEAR = "2015" # COPYRIGHT YEAR
CC_LICENSE = 'CC-BY'

STATIC_PATHS = ['images', 'pdfs']


