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
    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Latest Mars News
    mars["title"] = soup.find('div', class_='content_title').text.strip() 
    
    # Latest Mars paragraph
    mars["paragraph"] = soup.find('div', class_='rollover_description_inner').text.strip()
    
    # Featured Link
    mars["img_link"] = soup.find(class_='headerimage fade-in')['src']

    # Mars Table 
    mars_facts = pd.read_html('https://space-facts.com/mars/')
    df = mars_facts[0]
    html = df.to_html()
    mars['table'] = html

    # List of names - Mars Hemisphere
    # Grab all the titles 
    name_lists = []
    browser.visit(url2)

    for x in range (1,2):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')  

    name_dict = soup.find_all('h3')

    for x in name_dict:
        name_lists.append(x.text) 

    # Mars Hemispheres - Name 
    mars['names'] = name_lists

    # Image URLS - Mars Hemisphere 
    urls = []
    img_url = []
    browser.visit(url2)
    for name in name_lists:
        browser.click_link_by_partial_text(name)
    
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')  
        result = soup.find(class_='downloads')
    
        for x in result.find_all('a'):
            urlslink=x['href']
            urls.append(urlslink)
        img_url.append(urls[1])
        urls = urls[2:-2]
        browser.back()
    mars['url'] = img_url
    
    # Close the browser 
    browser.quit()

    # Return the result
    return mars
