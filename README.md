BASC Cache Fetcher
============

Simple Python set of scripts that obtain a list of a cached URLs for a website. This is important when the website suddenly goes offline for good, and leaves behind only Cached URLs. It support scraping from the following web caches (as of 2015-10-09):

* **Google Cache** - Google Cache is the most famous web cache system around. It obtains web caches from websites using GoogleBot crawlers to index metadata for searches.
  * **Listing** - The first step is to obtain all the cached URLs.
  * **Archival** - Because Google Cache has strong restrictions against robot scrapers, it is very difficult to grab more than 15 pages procedurally. However, there is a workaround: use Archive.is to archive the pages. Google has given this site exclusive rights to scrape the Google Cache without restriction, since they apparently understand the importance in saving certain cached pages.
* **Bing Cache** - Bing, another major search service, also makes cached URLs available to users. Bing has significantly fewer restrictions on robots, and does not prune dead caches as quickly, so it is the ideal webcache to work with.
  * **Listing** - Bing uses a very odd cache URL scheme, which obligates us to scrape the HTML. Thankfully, Bing is not prejudiced against robots, so this is quite an easy task.
  * **Archival** - Just use good ol' wget to grab the pages, with 1 second delay between requests.

### Why not use Bing API?

Unfortunately, Bing no longer provides cached URL ids in their API anymore. On the flip side, they are desparate for page views and allow any sort of traffic to come in their search engine, unlike Google, which is prejudiced against robots.

http://www.newmediacampaigns.com/page/search-microsoft-bing-with-xml-and-json-apis

Sign up free for 5,000 requests.