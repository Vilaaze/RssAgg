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

# # # # # # # # # # # # # 
# Replace All Characters
#
# s  = string to be rewritten
# li = list of characters to be replaced
# c  = value to replace with 
def replace_all(s, li, char):
	for c in li:
		s = s.replace(c, char)
	return s
# # # # # # # # # # # # # 

# # # # # # # # # # # # # 
# Assemble JSON
def assemble_json(entry):

		title = entry['title']
		summary = entry['summary']

		i = summary.find("<")
		# If there is HTML in the summary, get rid of it
		if(i != -1):
			summary =  summary[0:i]
		else:
			summary =  summary
		
		# Peel off ' " so it doesnt disrupt the JSON
		title = replace_all(title, ['\'', '"' ], '')
		summary = replace_all(summary, ['\'', '"'], '')

		
		s_JSON = '{"id": "'+ entry['id']  +'", "title": "'+ title  +'", "summary": "'+ summary +'", "link": "'+ entry['link'] +'"}'

		d_JSON = json.loads(s_JSON)
		return d_JSON


# # # # # # # # # # # # # 


# # # # # # # # # # # # # 
# Load JSON from file
#
# f_name = File Name of JSON database
#
# Open file
# Iterate through file and read JSON
def load_json(f_name):
	try:
		json_list = []
		f_db = open(f_name, 'r')
		for s in f_db:
			json_list.append(json.loads(s))
	
		f_db.close()
		return json_list

	except:
		print 'File ' + f_name + ' not found'
		return -1
# # # # # # # # # # # # # 


# # # # # # # # # # # # # 
# Load Links from file
# 
# f_name = Name of File to Read
#
# Reads file to end scanning in
# links into an array
#
def load_links(f_name):
	try:
		f_open = open(f_name, 'r')
		link_return = []
		for link in f_open:
			link_return.append(link.strip())
	
		f_open.close()
		return link_return
	except:
		print 'File ' + f_name + ' Not Found'
		return -1
# # # # # # # # # # # # # 


# # # # # # # # # # # # # 
# Main
# 
# 1. Get List of RSS Feed Links
# 2. Parse RSS feeds
# 3. Compile JSON objects from Feeds
# 4. Check to see if any new stories have been fetched
#
# Fetch all feed links from file
links = load_links('feeds.txt') 

# Parse all feeds
feeds = []
for s in links:
	feeds.append(feedparser.parse(s))

# Iterate through all feeds
j_list = []
for d in feeds:
	print d['feed']['title']
	print d['feed']['link']
	print d.feed.subtitle

	count = 0
	for entry in d['entries']:
		# Determine if there is a summary
		i = entry.summary.find("<")
		#if there isn't a summary (i == 0) then move on
		if(i != 0):
			d_json = assemble_json(entry)
			j_list.append(d_json)
			count = count + 1

	print str(count) + '/' + str(len(d['entries'])) + ' Story(s) detected'
	print
	
db = load_json('JSON.txt')

f_json = open("JSON.txt", "a")
count = 0
for j in j_list:
	exists = 0
	for j2 in db:
		if(j['link'].strip() == j2['link'].strip()):
			exists = 1

	if(exists == 0):
		f_json.write(json.dumps(j))
		f_json.write('\n')
		count = count + 1

f_json.close()

print str(count) + ' Story(s) saved'
