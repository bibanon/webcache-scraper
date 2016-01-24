from robobrowser import RoboBrowser
import re
import json
import time

fname = "cache.json"
site = "rockenflac.blogspot.com"			# site to search for
query = "site%3A" + site		# what to search for
total = 419						# the total amount of listings for this search on Bing 

browser = RoboBrowser()

listings = []
for i in range(1, total, 14):
	offset = i				# which listing to start at per page. Increment by 14
	browser.open('http://www.bing.com/search?q=%s&first=%d' % (query, offset))

	# Database Schema - A sqlite database is used to make data queries more efficient.
	# id (Primary Key) - ID of the item
	# orig_url - Original URL of the site.
	# cache_url - Cached URL of the site.
	# desc - Quick description of the site.

	# grab all search attribute strings
	capt_list = browser.select('.b_caption')
	for capt in capt_list:
		# start a new listing
		listing = {}
		
		# display original url
		listing['orig_url'] = re.sub('<[^>]*>', '', str(capt.select('cite')[0]))
		
		# display description
		listing['desc'] = capt.p.string
		
		# '|' delimited list, containing the ids needed to cache
		id_string = capt.select('div.b_attribution')[0].get('u')
		print(id_string)
		if (id_string != None):
			ids = id_string.split('|')
			listing['cache_url'] = "http://cc.bingj.com/cache.aspx?q=%s&d=%s&mkt=en-US&setlang=en-US&w=%s" % (query, ids[2], ids[3])
		else:
			listing['cache_url'] = None
		
		print(listing)
		listings.append(listing)
	
	print(":: End of dump %d" % i)
	
	# delay between page grabs
	time.sleep(1)

with open(fname, 'w') as outfile:
    json.dump(listings, outfile, sort_keys=True, indent=4, separators=(',', ': '))