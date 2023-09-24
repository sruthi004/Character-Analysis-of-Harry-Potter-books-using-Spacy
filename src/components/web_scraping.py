import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Creating web driver object
driver = webdriver.Chrome()
page_url = "https://harrypotter.fandom.com/wiki/Category:Character_indexes"
driver.get(page_url)

# Finding specific elements from the page (If we have cookie)
# from selenium.webdriver.common.by import By
# driver.find_element()

# Extracting data from web pages
# Books
from selenium.webdriver.common.by import By
books = driver.find_elements(By.CLASS_NAME, 'category-page__member-link') 
#print(books[6].text) # Books got extracted
#print(books[0].get_attribute('href')) # Links for books
driver.get(books[0].get_attribute('href')) # Access the link