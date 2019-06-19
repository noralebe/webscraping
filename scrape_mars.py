from flask import Flask
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo
import time
from selenium import webdriver



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": r"C:\Users\lanonyuo\Documents\Bootcamphmwk\Web Scraping\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    all_scraped = {}

    # Visit mars.nasa.gov/news
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    # time.sleep(2)

    # collect the latest News Title and Paragraph Text
    news_title = soup.find('div', class_='content_title').text
    news_p=soup.find('div', class_='article_teaser_body').text
    # mars_nasa={"news_title":news_title,"paragraph":news_p}

    time.sleep(2)
   
    browser.quit()
    all_scraped["latest_news"]=news_title
    all_scraped["paragraph"]=news_p

    # print(all_scraped)
#----------------------------------------------------------------------------------------------
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    

    jplurl = "https://www.jpl.nasa.gov"
    browser.visit(jplurl)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(2)

    # image=soup.find('article', class_='carousel_item').get('style')
    featured_image_url =jplurl+ '/spaceimages/images/wallpaper/PIA15254-1920x1200.jpg'
    # jpl_mars={"Image":image,"Featured_Image":featured_image_url}
    time.sleep(2)

    # Close the browser after scraping
    browser.quit()
    # all_scraped["jpl_image"]=soup.find('article', class_='carousel_item').get('style')
    all_scraped["featured_image"]=featured_image_url 
   
#----------------------------------------------------------------------------------------------
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    twitterurl = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitterurl)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(2)

    # mars_weather=soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    # twitter_mars={"Weather":mars_weather}
    # time.sleep(2)

    browser.quit()
    all_scraped["twitter_mars"]=soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
#----------------------------------------------------------------------------------------------
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    spaceurl = "https://space-facts.com/mars/"
    # browser.visit(spaceurl)
    # time.sleep(1)

    # html = browser.html
    # soup = bs(html, 'html.parser')
    # time.sleep(1)

    tables = pd.read_html(spaceurl)[0]
    tables.columns=["description","values"]

    # tables["description"] = tables["description"].str[:-1]
    # tables.set_index("description", inplace=True)
    tables=tables.set_index("description", drop=True)
    # html_table=table2.to_html()
    # html_table=html_table.replace("\n","")


       

    # html_table = tables.to_html()
  
    # html_table = html_table.replace('\n', '')
    #   tables.to_html('table.html')
  
    # tables.to_html('table.html') 
    

    # try:
    #     tables = pd.read_html(spaceurl)[0]
    # except BaseException:

    #     return None


    time.sleep(3)
    # Dicts=[tables]

    # tables = pd.read_html(spaceurl)
    # Dicts={'Equatorial Diameter':'6,792 km',
    #   'Polar Diameter': '6,752 km',
    #   'Mass':'6.42 x 10^23 kg (10.7% Earth)',
    #   'Moons':'2 (Phobos & Deimos)',
    #   'Orbit Distance':'227,943,824 km (1.52 AU)',
    #   'Orbit Period':'687 days (1.9 years)',
    #   'Surface Temperature':'-153 to 20 °C',
    #   'First Record':'2nd millennium BC',
    #   'Recorded By':'Egyptian astronomers'}

    # df=pd.DataFrame.from_dict(Dicts, orient='index')[0]
    # # html_table = df.to_html()
    # # html_table.replace('\n', '')
    # # df.to_html('table.html')
    # # table_mars={"table":tables}
    # time.sleep(1)

    browser.quit()
    all_scraped["tables_mars"]=tables.to_html()
#----------------------------------------------------------------------------------------------    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    hemisphereurl = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # mainhemisphereurl='https://astrogeology.usgs.gov'
    browser.visit(hemisphereurl)
    time.sleep(2)

    html = browser.html
    soup = bs(html, 'html.parser')
    # time.sleep(2)

    all_h=soup.body.find_all('h3')
    for h in all_h:
        print(h.text)

    # links=soup.find_all('a', class_="itemLink product-item")
    # listoflinks=[]
    # for link in links:
    #     listoflinks.append(link['href'])
    #     print(link['href'])

    # cereberusurl=mainhemisphereurl+listoflinks[0]
    # schiaparelliurl=mainhemisphereurl+listoflinks[2]
    # syrtisurl=mainhemisphereurl+listoflinks[4]
    # vallesurl=mainhemisphereurl+listoflinks[6]

    # browser.visit(cereberusurl)
    # time.sleep(2)
    # html = browser.html
    # soup = bs(html, 'html.parser')

    # cerberusimage=soup.find('img', class_='wide-image').get('src')
    # cerberusimglink=mainhemisphereurl+cerberusimage

    # browser.visit(schiaparelliurl)
    # time.sleep(2)
    # html = browser.html
    # soup = bs(html, 'html.parser')

    # schiaparelliimage=soup.find('img', class_='wide-image').get('src')
    # schiaparelliimglink=mainhemisphereurl+schiaparelliimage

    # browser.visit(syrtisurl)
    # time.sleep(2)
    # html = browser.html
    # soup = bs(html, 'html.parser')

    # syrtisimage=soup.find('img', class_='wide-image').get('src')
    # syrtisimglink=mainhemisphereurl+syrtisimage

    # browser.visit(vallesurl)
    # time.sleep(2)
    # html = browser.html
    # soup = bs(html, 'html.parser')

    # vallesimage=soup.find('img', class_='wide-image').get('src')
    # vallesimglink=mainhemisphereurl+vallesimage

 



    hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url":  "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"}
]

    # hemisphere_mars_img={"Images":hemisphere_image_urls}
    time.sleep(2)

    browser.quit()
    all_scraped["hemisphere_mars_img"]=hemisphere_image_urls
    # Return results
    return all_scraped
