#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Justin Lindsey'
AUTHOR_URL = 'disdanes_dev'
AUTHOR_SAVE_AS = ''
SITENAME = u'Chronobit Studios'
LUNAFORM_SITENAME = u'Lunaform'
SITESUBTITLE = (
    u'Small team with a big dream to make games like the ones we loved as '
    u'children.'
)
SITEURL = ''
LUNAFORM_SITEURL = "{}/{}".format(
    SITEURL,
    "lunaform_index"
)

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Pages
DISPLAY_PAGES_ON_MENU = False
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Pagination
DEFAULT_PAGINATION = 1000

# Author
DEFAULT_AUTHOR = 'Justin Lindsey'

# Categories
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'chronobit'
LUNAFORM_CATEGORY = 'lunaform'
PERSONAL_CATEGORY = 'disdanes'
USE_FOLDER_AS_CATEGORY = True

# Direct Templates for index pages
DIRECT_TEMPLATES = ((
    'index',
    'lunaform_index',
    'blog',
    'disdanes_dev'
))
PAGINATED_DIRECT_TEMPLATES = ((
    'index',
    'lunaform_index',
    'blog',
    'disdanes_dev'
))

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Themes
THEME = "chronobit"

# Menu Items
MENUITEMS = (
    ('Home', ''),
    ('Games', 'games'),
    ('Blog', 'blog'),
    ('Team', 'team'),
    ('Contact', 'contact'),
)

LUNAFORM_MENUITEMS = (
    ('Home', 'lunaform_index'),
    ('Play', 'lunaform/play'),
    ('Chronobit Studios', ''),
)


LUNAFORM_DESCRIPTION = """
Lunaform is a puzzle strategy game where your objective is to complete a hex
grid, by collecting stars of the same color.
"""

# Social Media
TWITTER_URL = "https://twitter.com/ChronobitStudio"
FACEBOOK_URL = "https://www.facebook.com/ChronobitStudios"
GOOGLE_PLUS_URL = "https://plus.google.com/101185014398199829755"
PINTEREST_URL = "http://www.pinterest.com/chronobitstudio/"
GITHUB_URL = "https://github.com/disdanes"

LUNAFORM_TWITTER_URL = "https://twitter.com/lunaformgame"
LUNAFORM_FACEBOOK_URL = "https://www.facebook.com/LunaformGame/"
