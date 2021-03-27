import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars = {}

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    browser.visit(url)

    # Results are returned as an iterable list 
    title = []
    paragraph = []
    results = soup.find_all('div', class_='slide')
    # Title
    for result in results: 
        # Identify and return title of listing 
        news_title = result.find('div', class_='content_title').text.strip() 
        title.append(news_title)
        # Identify and return paragraph of listing 
        news_p = result.find('div', class_='rollover_description_inner').text.strip()
        paragraph.append(news_p)
    # Latest Mars News
    mars["title"] = title[0]
    # Latest Mars paragraph
    mars["paragraph"] = paragraph[0]
    

    # # Featured Link
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')  
    link = soup.find(class_='headerimage fade-in')['src'] 
    featured_image_url= f"https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{link}"   
    mars["img_link"] = featured_image_url

    # Mars Hemishpere
    # Grab all the titles 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    name_lists = []

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    for x in range (1,2):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')  

        name_dict = soup.find_all('h3')

    for x in name_dict:
        name_lists.append(x.text) 

    mars['hemisphere_1'] = name_lists[0]
    mars['hemisphere_2'] = name_lists[1]
    mars['hemisphere_3'] = name_lists[2]
    mars['hemisphere_4'] = name_lists[3]


    # Grab all the urls 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    urls = []
    img_url = []

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # for y in range (1,2):
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')  

    for name in name_lists:
        browser.click_link_by_partial_text(name)
        
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')  
        result = soup.find(class_='downloads')
        
        for x in result.find_all('a'):
            urlslink=x['href']
            urls.append(urlslink)
        img_url.append(urls[0])
        urls = urls[2:-2]
        browser.back()

    mars['url1'] = img_url[0]
    mars['url2'] = img_url[1]
    mars['url3'] = img_url[2]
    mars['url4'] = img_url[3]
    return mars
