from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()

for i in range(1,4):
    driver.get(f'https://github.com/ProgrammingWithGaurav?page={i}&tab=repositories')
    try :
        elems = driver.find_elements(By.CLASS_NAME, 'col-lg-9')

        file = 0
        for elem in elems:
            a  = elem.get_attribute('outerHTML')
            with open(f'data/{i}-{file}.html', 'w', encoding='utf-8') as f:
                f.write(a)
                file += 1
        
        time.sleep(2)
    except Exception as e:
        print(e)

driver.close();