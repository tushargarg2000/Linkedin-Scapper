from selenium import webdriver

from bs4 import BeautifulSoup as bs

import os,random,sys,time
from urllib.parse import urlparse

from bs4 import BeautifulSoup

username = 'tushargarg0110@gmail.com'
password = 'Justdoit123.'

browser = webdriver.Chrome()


PROXY = "172.31.100.27:3128"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=chrome_options)


#
# browser.get('https://www.linkedin.com/uas/login')
#
# elementID = browser.find_element_by_id('username')
#
# elementID.send_keys(username)
#
# elementID = browser.find_element_by_id('password')
#
# elementID.send_keys(password)
#
# elementID.submit()

browser.get('https://www.linkedin.com/company/acciojob/people/')

SCROLL_PAUSE_TIME = 1.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



#Check out page source code
company_page = browser.page_source

#Use Beautiful Soup to get access tags
linkedin_soup = bs(company_page.encode("utf-8"), "html")
linkedin_soup.prettify()


print(linkedin_soup)

#Find the post blocks
#containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})

for a in linkedin_soup.find_all('a', href=True):
    var = "Found the URL:", a['href']
    print(var)
