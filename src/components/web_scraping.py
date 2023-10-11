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
time.sleep(3)
#driver.get(books[0].get_attribute('href')) # Access the link
#characters = driver.find_elements(By.CLASS_NAME, 'article-table') 
#print(characters[1].text)

# Creating a dictionary of books and URLs
books_url_dict = []
for category in books:
    book_url = category.get_attribute('href')
    book_name = category.text
    books_url_dict.append({'book_name':book_name, 'url':book_url})
print(books_url_dict)

# Extract characters
char_list = []
for book in books_url_dict:
    # go to book page
    driver.get(book['url'])
    
    char_elems = driver.find_elements(By.CLASS_NAME, 'article-table')
    for elem in char_elems:
        char_list.append({'book':book['book_name'],'character':elem.text})
char_list