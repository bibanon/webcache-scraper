# use unshortenit to remove adf.ly links
# https://pypi.python.org/pypi/unshortenit
import unshortenit

# Use python to grab all adf.ly links from all html files in a certain folder, then put them into JSON.
def restore(url):
    # attempt to unshorten
    unshortened_uri,status = unshortenit.unshorten(url)
    
    # verify if URL worked, then return unshortened
    if status == 200:
        return unshortened_uri
    else:
        return None

# extract adfly urls from all files in a folder
#def extract_urls(folder):
#	with open(path) as url_file:

def main():
	content = None
	with open("twitter.txt") as f:
		# grab urls from file and strip newlines 
		content = f.readlines()
		content = [x.strip('\n') for x in content] 
	
	for url in content:
		print(restore(url))

if __name__ == "__main__":
    main()