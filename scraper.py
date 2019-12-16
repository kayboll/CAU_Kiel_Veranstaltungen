# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import re
#
# # Read in a page
html = scraperwiki.scrape("http://www.uni-kiel.de/de/veranstaltungen/ueberblick")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
events = root.cssselect("div[class='news-list-item']")
for event in events:        # Second Example
    #elementDatePlaceTime = event.cssselect("div[class='news-list-item__dateline']")[0].text_content().strip().split("|")

    #print 'Date :',elementDatePlaceTime
    Time = event.cssselect("div[class='news-list-item__dateline']")[0][1].text
    Time = ''.join(Time.split())
    Time = Time.split("|")
    Time = " | ".join(Time)
    
    Title = event.cssselect("h3[class='ce-headline-h4']")[0].cssselect("span")[0].text
    print Title.encode("ascii")
    print Time.encode("ascii")
    scraperwiki.sqlite.save(unique_keys=['title'], data={"title": Title, "time": Time})

  
# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
scraperwiki.sql.select("* from data")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
