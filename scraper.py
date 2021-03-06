# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://www.uni-kiel.de/de/veranstaltungen/ueberblick")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
events = root.cssselect("div[class='news-list-item']")
for event in events:  
    Time = event.cssselect("div[class='news-list-item__dateline']")[0][1].text.strip()
    Time = " ".join(Time.split())
    Title = event.cssselect("h3[class='ce-headline-h4']")[0].cssselect("span")[0].text
    print Title.encode('utf-8')
    print Time.encode('utf-8')
    scraperwiki.sqlite.save(unique_keys=['title'], data={"title": Title, "time": Time})

  
scraperwiki.sql.select("* from data")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
