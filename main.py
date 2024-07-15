from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.get('https://python.org/')

# find title of the page
assert "Python" in driver.title
# find element by name
elem = driver.find_element(By.NAME, 'q') # find search box
elem.send_keys('pycon') # enter pycon in search box
elem.send_keys(Keys.RETURN) # hit return after entering pycon

# check if the page title is correct
assert "No results found." not in driver.page_source
time.sleep(6)
driver.close()