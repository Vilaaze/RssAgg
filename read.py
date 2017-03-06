
import json

db = []
try:
	f_db = open("JSON.txt", "r")
	for s in f_db:
		db.append(json.loads(s))
	
	f_db.close()

except:
	print "No existing JSON"

for story in db:
	print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----'
	print story['title'], ':'
	print

	print story['summary']
	print story['link']
	print
