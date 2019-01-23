# Web_Scrapping
This is the repository that deals with Splinter (Web driver), Pymongo -Flask and HTML.
A web application which scrapes data from five different websites to gather data related to the Mission to Mars and displays the information in a single HTML page.

Scraping:

- https://mars.nasa.gov/news/ website was used to get the latest news on Mars mission using BeautifulSoup, splinter, pandas in a jupyter notebook.
- https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars was used to scrape the featured image of mars in full resolution.
- https://twitter.com/marswxreport?lang=en was used to get the latest tweet on the mars weather.
- https://space-facts.com/mars/ to gather the facts table about Mars
- https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to get the images of 4 hemispheres of Mars


Python & Mongo integrating Flask:

A python script to run all of the scraping code was designed and all gathered data was put into one Python dictionary.

A route '/scrape' which imports the Python script and calls the scrape function.

A new database and a new collection was created where all scaped data was stored.

Root route / that queries the database and pass the mars data into HTML template was created.

HTML and BootStrap:

A page 'index.html' was designed to display all scraped data elements.
