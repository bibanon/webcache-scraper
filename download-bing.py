import json
# writes the JSON data to a text file for wget to grab

def extract_cache_urls(listings, path):
	# write the cache URLs to a text file
	with open(path, 'w') as url_file:
		for listing in listings:
			if (listing['cache_url'] != None):
				url_file.write(listing['cache_url'] + '\n')

def main():
	in_fname = 'cache.json'
	out_fname = 'cache-urls.txt'
	
	with open(in_fname) as json_file:
		listings = json.load(json_file)
		extract_cache_urls(listings, out_fname)

if __name__ == "__main__":
	main()