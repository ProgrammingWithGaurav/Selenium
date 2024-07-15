from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
query = 'ProgrammingWithGaurav'
driver.get(f'https://github.com/{query}')

elems = driver.find_elements(By.CLASS_NAME, 'heading-element')
print(len(elems))
for elem in elems:
    print(elem.text)

time.sleep(2)
driver.close()