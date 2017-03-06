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

import feedparser
import json

def rep_all(s, li, char):
	for c in li:
		s = s.replace(c, char)

	return s

# Fetch all feed links from file
file_feeds = open("feeds.txt", "r")
feeds = [] 

# Parse all feeds
for s in file_feeds:
	feeds.append( feedparser.parse(s) )

file_feeds.close()

j_list = []
# Iterate through all feeds
for d in feeds:
	print d['feed']['title']
	print d['feed']['link']
	print d.feed.subtitle
	print len(d['entries'])
	index = 0

	#  Assemble JSONs from all Stories from each feed
	for entry in d['entries']:
#		print entry.viewkeys()

		# Determine if there is a summary
		i = entry.summary.find("<")
		index = index + 1
		#if there isn't a summary (i == 0) then move on
		if(i != 0):
			title = rep_all(entry.title, ['\'', '"' ], '')
			
			# If there is HTML in the summary, get rid of it
			if(i != -1):
				s =  entry.summary[0:i]
			else:
				s =  entry.summary
			
			# Peel off ' " so it doesnt disrupt the JSON
			s = rep_all(s, ['\'', '"'], '')

		# Form the string for the JSON
		s_JSON = '{"id": "'+ entry.id  +'", "title": "'+ title  +'", "summary": "'+ s +'", "link": "'+entry.link+'"}'

		d_JSON = json.loads(s_JSON)
#		print "TITLE: " +  d_JSON['title']
		j_list.append(d_JSON)

db = []
try:
	f_db = open("JSON.txt", "r")
	for s in f_db:
		db.append(json.loads(s))
	
	f_db.close()

except:
	print "No existing JSON"

f_json = open("JSON.txt", "a")
for j in j_list:
	exists = 0
	for j2 in db:
		if(j['link'].strip() == j2['link'].strip()):
			exists = 1

	if(exists == 0):
#		print j['title']
		f_json.write(json.dumps(j))
		f_json.write('\n')

f_json.close()
