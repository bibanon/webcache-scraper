from google import search

out_fname = 'moe-google-cache.txt'
total = 500							# total amount of entries in the search
delay = 5							# time between page scraping


# write the cache URLs to a text file
with open(out_fname, 'w+') as url_file:
	# obtain the search urls and write them to file
	for url in search('site:archive.moe', stop=total, pause=delay):
		if (url != None):
			# create cache url
			cache_url = 'http://webcache.googleusercontent.com/search?q=cache:%s' % url
			
			# display url
			print(cache_url)
			
			# save to file
			url_file.write(cache_url + '\n')