#
# RSS Reader and Aggregator
#
# Brian John Sedwick Reeder
# reeder.brian.j@gmail.com
#
# The goal of this application is to fetch
# RSS feeds and aggregate similar articles
# under one header from multiple news sources
# so that the user is not encumbered with
# having to read through multiple publications
# of the same topic

from util import *

from read import *

import feedparser
import json

# # # # # # # # # # # # # 
# Main
# 
# 1. Get List of RSS Feed Links
# 2. Parse RSS feeds
# 3. Compile JSON objects from Feeds
# 4. Check to see if any new stories have been fetched
# 5. Update DB appropriately
# 6. Print all story cards
#
# Fetch all feed links from file
links = load_links('feeds.txt') 

# Parse all feeds
feeds = []
for s in links:
	feeds.append(feedparser.parse(s))
# Iterate through all feeds
j_list = justify_stories(feeds)	
db = update_db('JSON.txt', j_list)

for entry in db:
	display_story(entry)
