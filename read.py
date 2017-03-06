
import json
dict_r = []

f_dict = open("dict_r.txt", "r")
for word in f_dict:
	dict_r.append(word)

f_dict.close()

dict_p = []
f_dict = open("dict_p.txt", "r")
for punc in f_dict:
	dict_p.append(punc)

f_dict.close()

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
	
	title = story['title']
	summ = story['summary']
	for word in dict_r:
		title = title.replace(' '+word.strip()+' ', ' ')
		summ = summ.replace(' ' + word.strip() + ' ', ' ')

	for punc in dict_p:
		title = title.replace(punc.strip(), '')
		summ = summ.replace(punc.strip(), '')
	
	print title, ':'
	print

	print summ
	print story['link']
	print

