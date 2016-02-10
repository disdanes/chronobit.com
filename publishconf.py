#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = ''
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "chronobitstudios"
GOOGLE_ANALYTICS = "UA-47262702-1"

PAGE_SAVE_AS = '{slug}'
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}'
LUNAFORM_INDEX_SAVE_AS = 'lunaform_index'
BLOG_SAVE_AS = 'blog'
DISDANES_DEV_SAVE_AS = 'disdanes_dev'
