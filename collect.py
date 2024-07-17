from bs4 import BeautifulSoup
import os
import pandas as pd

dictionary = {
    'title': [],
    'date': [],
    'desc': [],
    'programming_language': []
}

for file in os.listdir('data'):
    with open(f'data/{file}') as f:
        html_doc = f.read()
    try :
        soup = BeautifulSoup(html_doc, 'html.parser')
        title = soup.find('a').get_text()
        desc = soup.find('p', attrs={"itemprop": "description"}).get_text()
        programming_language = soup.find('span', attrs={"itemprop": "programmingLanguage"}).get_text()
        date = soup.find('div', attrs={"class": "color-fg-muted"}).find('relative-time').get_text()

        # print(title, date, desc, progrsamming_language)
        
        dictionary['title'].append(title)
        dictionary['date'].append(date)
        dictionary['desc'].append(desc)
        dictionary['programming_language'].append(programming_language)
    except Exception as e:
        print(e)
        
# df = pd.DataFrame(dictionary)
# df.to_csv('data.csv', index=False)
