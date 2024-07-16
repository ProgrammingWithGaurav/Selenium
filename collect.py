from bs4 import BeautifulSoup
import os

# d = {num: }

for file in os.listdir('data'):
    with open(f'data/{file}') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    t = soup.find('p')
    num = t.get_text()
    print(num)