#!/bin/bash
# script to upload websites from a file into archive.is.
# Usage: upload-archive-is.sh <file-with-urls.txt>

# If using this script to archive Google Cache, don't panic if you notice that
# it trips the Google robot blocker: Google has given Archive.is a special
# exemption to scrape the cache, which is why we use it for this case.

# curl script by Michael Nelson
# https://groups.google.com/d/msg/memento-dev/XVAVyqyr9xQ/lMG2t77YW24J

# file reader loop by cppcoder
# http://stackoverflow.com/questions/10929453/bash-scripting-read-file-line-by-line

# use curl to submit the URL directly to archive.is on a 5 second delay
while IFS='' read -r line || [[ -n "$line" ]]; do
    curl -i -d url=$line http://archive.is/submit/
    sleep 5
done < "$1"
 
