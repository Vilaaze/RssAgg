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

#d = feedparser.parse('http://www.reddit.com/r/python/.rss')
feeds = {
	feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml'),
	feedparser.parse('http://rss.cnn.com/rss/cnn_world.rss') 
}

for d in feeds:
#	print d.feed.viewkeys()

	print d['feed']['title']
	print d['feed']['link']
	
	print d.feed.subtitle
	
	print
	print len(d['entries'])
	print

	
	for entry in d['entries']:
		print
		print "---- ---- ---- ----"
		print "|" + entry.id
		print "|" + entry.title
		
		i = entry.summary.find("<")
		if(i != -1):
			print "|" + entry.summary[0:i]
		else:
			print "|" + entry.summary
		print "---- ---- ---- ----"
