import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
# import time
# from fake_useragent import UserAgent

url = 'https://www.imperial-library.info/books/all/by-category'
page = rq.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

for x in soup.find_all('a'):
    print(x.text)
    
titles = []
for x in soup.find_all("page-title"): 
  titles.append(x.text)

links = []
for link in soup.find_all("a"):
  links.append(link.get('href'))


print(titles)
print(links)


links.remove("http://www.elderscrolls.com/")
links.remove("http://www.bethsoft.com/")
links.remove("http://www.zenimax.com/")
print (links)

full_link = []
for i in range(len(links)):
  url=('https://www.imperial-library.info'+ (str(links[i])))
  full_link.append(url)

print(full_link)

# ########################################################################
import pandas as pd
data = []
df = pd.DataFrame(data, columns=["contents"])
texts = []

try:
  for url in full_link:
    book_contents=rq.get((url))
    book_contents.encoding = 'utf-8'
    soup = BeautifulSoup(book_contents.text, features="html.parser")
    print(soup.prettify(book_contents))
    texts.append(soup.text)
except:
  pass

with open("HP.json", "w") as file:
    for x in soup.find_all("a"):
        t = x.text.strip() + "\n"
        file.write(t)
        # print('Done')
####################################################

import nltk
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger_en')
nltk.download('universal_tagset')
import re
import spacy

with open('C:\\Users\\linki\\Desktop\\KT\\HP_new.json', encoding='utf-8') as text:
    imperial_library_raw = text.read()

imperial_library = imperial_library_raw.replace("[\]|[\n]| [The Imperial Library]|[Skip navigation]", "")
print(imperial_library)                
                                                
# ###########################
imperial_library = imperial_library_raw.replace("","")
print(imperial_library)

#     #################
imperial_library_lowercase=imperial_library_raw.lower()
tokenizer = RegexpTokenizer(r'\w+')
imperial_library_tokenized=tokenizer.tokenize(imperial_library_lowercase)


nltk.download('stopwords')
stopwords_list=stopwords.words('english')

imperial_library_cleared = []
 
for token in imperial_library_tokenized:
    if token not in stopwords_list:
        imperial_library_cleared.append(token)

stopwords_list_extended = ['url', '0', 'null', 'title', 'text',  'n', 'nskip', 'navigation', 'CD', 'library', 'elder', 'scrolls', 'u2019s', 'money', 'u2014', 'would', 'could', 'like', 'nlogin', 'profile', 'nstoryboard', 'nrecent', 'posts', 'n', 'ntopics', 'nrandom', 'nhelp', 'desk', 'n', 'spacer', 'npocket', 'guidesfirst', 'edition', 'nthird', 'nemperor', 'ngame', 'booksall', 'narena', 'ndaggerfall', 'nbattlespire', 'nredguard', 'nmorrowind', 'nshadowkey', 'noblivion', 'nskyrim', 'nonline', 'nstorylinesarena', 'ndaggerfall', 'nbattlespire', 'nredguard', 'nmorrowind', 'ndawnstar', 'nshadowkey', 'nstormhold', 'noblivion', 'noblivion', 'mobile', 'nskyrim', 'nonline', 'nlegends', 'nblades', 'nnovelsthe', 'ninfernal', 'nlord', 'nagents', 'ngathering', 'nkyne', 'nnaryu', 'nthe', 'ngeography', 'historytamriel', 'ntamriel', 'timeline', 'ncartographytamriel', 'nblack', 'ncyrodiil', 'nelsweyr', 'nhammerfell', 'nhigh', 'nmorrowind', 'nskyrim', 'nsummerset', 'nvalenwood', 'nother', 'noblivion', 'ncities', 'nguide', 'nnotes', 'nmajor', 'npeople', 'societyraces', 'nkhajiit', 'nguide', 'nguide', 'nguide', 'nguilds', 'nitems', 'nantiquities', 'nlgbtq', 'n', 'nlanguage', 'artsgallery', 'tesarena', 'ndaggerfall', 'nbattlespire', 'nredguard', 'nmorrowind', 'noblivion', 'nskyrim', 'ntamrielic', 'alphabetsakaviri', 'script', 'naldmeri', 'alphabets', 'nancient', 'ndaedric', 'ndivine', 'ndragon', 'alphabet', 'nelder', 'nmage', 'ntranslation', 'dictionarydragon', 'njel', 'nkothri', 'nriekling', 'nta', 'agra', 'nreligion', 'ngenesis', 'nthe', 'nguide', 'ndevelopersobscure', 'texts', 'nthe', 'interviews', 'npost', 'archives', 'nthread', 'nmad', 
'nwho', 'nspecial', 'collectionswebsite', 'content', 'ncut', 'content', 'nbook', 'ngo', 'ntes', 'ndog', 'homework', 'nthe', 'elderscrolls', 'ngame', 'data', 'ncommunity', 'archivesaffa', 'works', 'ncritical', 'nloranna', 'rp', 'nmorrowind', 'npocket', 'ncollaborationabout', 'us', 'ntes', 'elsewhere', 'nforum', 'n20th', 'anniversary', 'art', 'n20th', 'anniversary', 'fiction', 'n', 'nhome', 'nsubmitted', 'nfiction', 'nnocturnal', 'ntes4', 'ntes5', 'author', 'u00a0', 'u00a0', 'nthe', 'u00a9', 'imperial', 'series', 'trademarks', 'bethesda', 'softworks', 'llc', 'zenimax', 'media', 'company', 'rights', 'reserved']

imperial_library_refined = []
 
for token in imperial_library_cleared:
    if token not in stopwords_list_extended:
        imperial_library_refined.append(token)

print(imperial_library_refined)


frequency_distribution = FreqDist(imperial_library_refined)
frequency_list_graph = frequency_distribution.plot(200, cumulative=False)
print(frequency_list_graph)

imperial_library_tagged= nltk.pos_tag(imperial_library_refined, lang='eng')
print (imperial_library_tagged)

############################################
import nltk
from nltk.collocations import *
bigram_assoc_measures = nltk.collocations.BigramAssocMeasures()
from collections import Counter

bigrams = nltk.bigrams(imperial_library_refined)
for bigram in bigrams:
  print(bigram)

trigrams = nltk.trigrams(imperial_library_refined)
for trigram in trigrams:
  print(trigrams)

################ IN PROGRESS #################################################################
# imperial_library_refined_new =(str(imperial_library_refined))
# # imperial_library_refined_new = text.split()
# minimum_number_of_bigrams = 2
# top_bigrams_to_return = 5
# finder = BigramCollocationFinder.from_words(imperial_library_refined_new)
# finder.apply_freq_filter(minimum_number_of_bigrams)
# topcollocations=finder.nbest(bigram_assoc_measures.pmi, top_bigrams_to_return)
# # print(topcollocations)

#########################################################
# from sklearn.feature_extraction.text import TfidfVectorizer

# tfidf_vectorizer = TfidfVectorizer(stop_words="english")
# tfidf = TfidfVectorizer.fit_transform('C:\\Users\\linki\\Desktop\\KT\\ilr.txt'.status) 
# tfidf.shape
# print(tfidf)

# contents = []
# for link in soup.find_all("div.node-content.clear-block.prose"):
#   links.append(link.get('href'))
# print(contents)
