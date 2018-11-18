from splinter import Browser
from bs4 import BeautifulSoup
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    # mars_scrapped_data = {}

    url= 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html= browser.html
    soup = BeautifulSoup(html, 'html.parser') 
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    
    # just to check the output
    print(f"Title: {news_title}")
    print(f"Paragraph: {news_p}")

    url_image= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(3)
    browser.click_link_by_partial_text('more info')
    new_html= browser.html
    imgsoup = BeautifulSoup(new_html, 'html.parser')
    temp_img = imgsoup.find('img', class_='main_image')['src']

    featured_image_url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars' + temp_img
    print(featured_image_url)

    mars_twitter_url= 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter_url)

    mars_twitter= browser.html
    soup = BeautifulSoup(mars_twitter, 'html.parser') 
    find_tweet = soup.find('p', class_='TweetTextSize').text
    mars_weather= find_tweet
    print(f"Latest Tweet: {mars_weather}")

    
    
    mars_facts_url = 'https://space-facts.com/mars/'
    
    tables = pd.read_html(mars_facts_url)
    tables
    

    df = tables[0]
    df.columns = ['Profile', 'Details']
    df.head()
    df.set_index('Profile', inplace=True)
    df.head()
    html_table = df.to_html()
    html_table
    html_table.replace('\n', '')

    df.to_html('table.html')


    url_mars= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars)
    
    hemi_dicts = []

    for i in range(1,9,2):
        hemi_dict = {}
    
        browser.visit(url_mars)
    #     time.sleep(1)
        hemispheres_html = browser.html
        hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')
        hemi_name_links = hemispheres_soup.find_all('a', class_='product-item')
        hemi_name = hemi_name_links[i].text.strip('Enhanced')
    
        detail_links = browser.find_by_css('a.product-item')
        detail_links[i].click()
        time.sleep(1)
        browser.find_link_by_text('Sample').first.click()
        time.sleep(1)
        browser.windows.current = browser.windows[-1]
        hemi_img_html = browser.html
        browser.windows.current = browser.windows[0]
        browser.windows[-1].close()
    
        hemi_img_soup = BeautifulSoup(hemi_img_html, 'html.parser')
        hemi_img_path = hemi_img_soup.find('img')['src']

        print(hemi_name)
        hemi_dict['title'] = hemi_name.strip()
    
        print(hemi_img_path)
        hemi_dict['img_url'] = hemi_img_path

        hemi_dicts.append(hemi_dict)

    mars_scrapped_data ={"news_title": news_title, 
                        "news_paragraph": news_p,
                        "featured_image": featured_image_url,
                        "Latest_Tweet": mars_weather,
                        "Hemispheres_details": hemi_dicts,
                        # "Table": html_table
                        }
    return mars_scrapped_data