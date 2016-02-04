#!/usr/bin/python3
# script to upload certain Google Cache URLs into archive.is.
# Start replacing it with real Google API or else we won't be able to make it
# https://developers.google.com/api-client-library/python/start/installation

# Custom search over one site: https://github.com/google/google-api-python-client/blob/master/samples/customsearch/main.py
# you must create a custom search first and get an api key before continuing: https://developers.google.com/custom-search/docs/tutorial/creatingcse?hl=en
# Other Samples: https://github.com/google/google-api-python-client/blob/master/samples/README.md

# If using this script to archive Google Cache, don't panic if you notice that
# Archive.is trips the Google robot blocker: Google has given Archive.is a special
# exemption to scrape the cache, which is why we use it for this case.

# Dependencies: pip3 install --upgrade google-api-python-client
import pickle
import docopt
from google import search

__doc__ = """google-it.py - Gather all search results from a query.

Usage:
  google-it.py <query> <total>
  google-it.py <query> <total> --delay <wait>
  google-it.py --continue
  google-it.py -h | --help
  google-it.py --version

Arguments:
  <query>       Standard Google search query.
  <total>       Total items in the query (find from last page)
                Cannot be larger than 1000...

Options:
  -h --help       Show this screen.
  --version       Show version.
  --continue      Continue a previous scrape.
  --delay <wait>  How long to wait before next scrape. [default: 5]
"""

# write all the lines in an object to a file, line by line
def write2file(obj, fname):
    # write the cache URLs to a text file
    with open(fname, 'w+') as f:
        for element in obj:
    		# save to file
            f.write(element + '\n')

# use the basic google listing scraper
def get_listings(query, start, total, delay):
	# obtain the search urls and add them to an array
	# catch HTTPError 503: if so, pickle the generator for later use. http://stackoverflow.com/questions/8778340/can-a-python-generator-be-easily-saved-and-reloaded-from-disk
	urls = []
	for url in search(query, start=start, stop=total, pause=delay):
		if (url != None):
			# create cache url
			cache_url = 'http://webcache.googleusercontent.com/search?q=cache:%s' % url
			
			# display url
			print(cache_url)
			
			urls.append(cache_url)
		else:
		    print('No urls found.')
	
	# return array
	return urls
	
def main():
    query = 'site:warosu.org'
    total = 685							# total amount of entries in the search
    delay = 5							# time between page scraping
    start = 0
    out_fname = 'warosu-google-cache.txt'
    
    # either extract the variable "stop" from the generator, or pickle the entire generator (requires pypy)
    listings = get_listings(query, start, total, delay)
    write2file(listings, out_fname)
    
if __name__ == "__main__":
    main()