import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import time

# STEP 1
texts = []
all_page = ['https://sysblok.ru']
for i in range(16):
  all_page = rq.get('https://sysblok.ru/page/2')
  all_page.encoding = 'utf-8'

soup = BeautifulSoup(all_page.text, features="html.parser")

texts.append(soup.text)
print(texts)

# STEP 2
all_links = []

for link in soup.find_all('a' in 'h2'):
    all_links.append(link.get('href'))

all_links
print(all_links)


# STEP 3
main_page = ['https://sysblok.ru/page/1']
print(soup.find('time').text)

title = []

for link in soup.find_all('title' in 'h1'):
    title.append(link.get('title'))

print(title)

for x in soup.find_all('p'):
    print(x.text)

authors=[]
for link in soup.find_all("author-block__name" in 'h2'):
    title.append(link.get("href"))
authors
print(authors)

# STEP 4
for i in range(1,16):
    print(100/i)

print('Должно работать без проблем')

source_for_parsing = ['sysblok']

for address in source_for_parsing:
    try:
        page_response = rq.get(f'https://sysblok.ru')
        current_html = BeautifulSoup(page_response.text, features="lxml")
        print(current_html.title)
    except:
        print(f'Страница https://{address}.ru упрямится')
