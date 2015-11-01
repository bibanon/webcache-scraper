import json
# writes the JSON data to a text file for wget to grab

in_fname = 'cache.json'
out_fname = 'cache-urls.txt'
with open(in_fname) as json_file:
	listings = json.load(json_file)
	
	# write the cache URLs to a text file
	with open(out_fname, 'w') as url_file:
		for listing in listings:
			if (listing['cache_url'] != None):
				url_file.write(listing['cache_url'] + '\n')
