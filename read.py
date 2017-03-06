#
# Brian John Sedwick Reeder
#
# Read in JSON and strip out
# indistinct words and punctuation

def load_d(f_name):
	try:
		f_dict = open(f_name, 'r')
		nd = []
		for word in f_dict:
			nd.append(word.strip())
	
		f_dict.close()
	except:
		print f_name, ' not found...'
		nd = -1

	return nd

import json

dict_r = load_d('dict_r.txt')
dict_p = load_d('dict_p.txt')

db = []
try:
	f_db = open('JSON.txt', 'r')
	for s in f_db:
		db.append(json.loads(s))
	
	f_db.close()

except:
	print 'No existing JSON'

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

