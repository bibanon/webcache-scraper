#!/usr/bin/python3
# Bing Cache Archiver
# Written by Antonizoon for the Bibliotheca Anonoma

# pip3 install robobrowser docopts
from robobrowser import RoboBrowser
import re
import json
import time
import docopt

# store input variable as JSON file
def store_json(obj, path):
	# write to JSON, pretty printed
	with open(path, 'w') as outfile:
		json.dump(obj, outfile, sort_keys=True, indent=2, separators=(',', ': '))

# scrape bing's HTML search results
def scrape_cache(query, total):
	
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
	
	# listings is given as an output object
	return(listings)

# writes the JSON data to a text file for wget to grab
def extract_cache_urls(listings, path):
	# write the cache URLs to a text file
	with open(path, 'w') as url_file:
		for listing in listings:
			if (listing['cache_url'] != None):
				url_file.write(listing['cache_url'] + '\n')

def main():
    # parameters
	site = "dromble.com"			# site to search for
	query = "site%3A" + site		# what to search for
	total = 47						# the total amount of listings for this search on Bing 
	
	# Filenames
	json_fname = 'listings.json'
	cache_fname = 'cache-urls.txt'
	
	# scrape the search results
	listings = scrape_cache(query, total)
	
	# store the listings to JSON
	store_json(listings, json_fname)
	
	# write cache urls only to text file for easy scrape with wget
	with open(json_fname) as json_file:
		listings = json.load(json_file)
		extract_cache_urls(listings, cache_fname)

	print("Done. Now use the following wget command to archive the cached pages:")
	print("wget -p -k -i cache-urls.txt -e robots=off")

if __name__ == "__main__":
    main()