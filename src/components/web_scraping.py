import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Creating web driver object
driver = webdriver.Chrome()
page_url = "https://shadowhunters.fandom.com/wiki/Chain_of_Gold"

driver.get(page_url)