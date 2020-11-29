import requests
import pandas as pd
import pymongo
import os
import time
from bs4 import BeautifulSoup as init_browser
import splinter
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    # !which chromedriver

    executable_path = {"executable_path": ChromeDriverManager().install()}
    # executable_path = {'executable_path': '/Applications/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():

    browser = init_browser()
    # create mars_data dict/list? that we can insert into mongo

    # get Mars headline
    mars_headline = (
        "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&year=2020%3Apublish_date&category=19%2C165%2C184%2C204&blank_scope=Latest'"
    )
    browser.visit(mars_headline)

    # grab headline
    headline_url = browser.find_("content_title").first["href"]
    browser.visit(headline_url)
    browser.is_element_present_by_css("rollover_description_inner", 1)

    # create soup object from html
    html = browser.html
    report = BeautifulSoup(html, "html.parser")

    time.sleep(1)

    mars_headline_report = soup.find('div', class_="image_and_description_container").find('div', class_='content_title').text
    mars_para_report = soup.find('div', class_="image_and_description_container").find('div', class_='content_title').text
    #report.find_all("p")

    # add it to our mars data dict
    mars_headline["report"] = build_report(mars_report)

    # return our mars data dict

    mars_img = {}

    # visit url
    jpl_img_url_start = 'https://www.jpl.nasa.gov/spaceimages'
    mars_img = browser.find_by_id('jpl_img_url_start')
    url_start = "mars_img"
    browser.visit(jpl_img_url_start)
    browser.is_element_present_by_id("gridMulti", 1)
    html = browser.html
    soup = bs(html, 'html.parser')

    # create a soup object from the html
    img_soup = BeautifulSoup(html, "html.parser")
    img_src = img_soup.find(id="gridMulti")
    featured_img_src = elem.find("img")["src"]

    # add our src to mars data with a key of src
    mars_data["src"] = img_src

    #mars_data
    mars_data_url = 'https://space-facts.com/mars'
    mars_facts_table = pd.read_html(mars_data_url)

    #convert to dataframe
    mars_facts_df = mars_facts_table[0]
    mars_facts_df = mars_facts_df.rename(columns={0:"Mars Profile", 1 : " "})

    #section on hemispheres

    <div class="container">
        <div class="row">
          <div class="col-md-8 col-md-offset-2">
    #           <img src= {{hemisphere_image_url1.src}}/>
    #           <img src= {{hemisphere_image_url2.src}}/>
    #           <img src= {{hemisphere_image_url3.src}}/>
    #           <img src= {{hemisphere_image_url4.src}}/>
                <hemisphere_img_src= {{hemisphere_image_urls.src}}/>
            <h3>Hemispheres</h3>
            <p>{{ hemisphere_img_url.report}}</p>
          </div>
      </div>

    hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
]

    for url in hemisphere_image_urls:
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        url = soup.find('li')
        img_url = url.find('a')['href']

        hemispheres_img_src = soup.find(class_ = 'img_id').text
        img_images.append({"title": title, "img_url": img_url})

    mars_dict = {
        "mars_headline_report" : mars_headline_report,
        "mars_para_report" : mars_para_report,
        "featured_img_src" : featured_img_src,
        "mars_facts_df" : mars_facts_df,
        "hemispheres_img_src" : hemispheres_img_src
    }

    browser.quit()

    return featured_img_src
    return mars_data
    return mars_dict
    return hemispheres_img_src
    

