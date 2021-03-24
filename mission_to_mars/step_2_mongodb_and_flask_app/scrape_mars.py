import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars = {}

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars["title"] = soup.find('div', class_='content_title').text.strip() 
    mars["paragraph"] = soup.find('div', class_='rollover_description_inner').text.strip()
    mars["img_link"] = soup.find(class_='headerimage fade-in')['src']
    browser.quit()

    # List of names - Mars Hemisphere
    # Grab all the titles 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    name_lists = []

    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url2)

    for x in range (1,2):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')  

        name_dict = soup.find_all('h3')

    for x in name_dict:
        name_lists.append(x.text) 

    print(name_lists)
    # Quit the browser

    browser.quit()

    return listings
