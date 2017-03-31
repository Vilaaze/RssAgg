#
# Brian John Sedwick Reeder
#
# Read in JSON and strip out
# indistinct words and punctuation

###########################################
# Load Dictionary
#
# Read Dictionary of words, characters
# from a file into an array
#
def load_d(f_name):
        # Attempt to open file
	try:
		f_dict = open(f_name, 'r')
		nd = []
                # Get each word from file
		for word in f_dict:
                        # Take all leading and trailing whitespace
                        # off of word. 
                        # Add lower-case and Title-case
			nd.append(word.strip())
			nd.append(word.strip().title())
	
		f_dict.close()
	except:
		print f_name, ' not found...'
		nd = -1

	return nd
###########################################

import json


###########################################
# 
# Display Story
#
# Print out individual cards for each story
def display_story(story):
	print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----'
	
	dict_r = load_d('dict_r.txt')
	dict_p = load_d('dict_p.txt')
		
	title = story['title']
	summ  = story['summary']
	
	# Sanitize each sentence of each word and punctuation
	for word in dict_r:
		n_word = ' ' + word.strip() + ' '
		title = title.replace(n_word, ' ')
		summ  = summ.replace(n_word, ' ')
	
	title = title.replace('U.S. ', 'United States ')
	summ = summ.replace('U.S. ', 'United States ')
	title = title.replace('US ', 'United States ')
	summ = summ.replace('US ', 'United States ')
	title = title.replace('E.U. ', 'European Union ')
	summ = summ.replace('E.U. ', 'European Union ')
	title = title.replace('EU ', 'European Union ')
	summ = summ.replace('EU ', 'European Union ')
	
	
	title = title.replace('U.N. ', 'United Nations ')
	summ = summ.replace('U.N. ', 'United Nations ')
	title = title.replace('UN ', 'United Nations ')
	summ = summ.replace('UN ', 'United Nations ')
	
	for p in ['.', '!', '?']:
		title = title.replace(p, ' ')
		summ = summ.replace(p, ' ')
		
	
	for punc in dict_p:
		title = title.replace(punc.strip(), ' ')
		summ = summ.replace(punc.strip(), ' ')
			
	title = title.replace('  ', ' ')
	summ = summ.replace('  ', ' ')
		
	# Display Sanitized Text
	print title, ':'
	print
	
	print summ
	print story['link']
	print
###########################################
