import urllib.request as req   # the request object
resp=req.urlopen("https://www.python.org")
text=resp.read()
tokens_by_split=text.split()

import re
text=str(text,'utf8')
tokens_by_re=re.split(r'\W+', text)

import nltk
import bs4
clean_html_text=bs4.BeautifulSoup(text).getText()
tokens_by_cleaned_split=[token for token in clean_html_text.split()]

freq_by_nltk=nltk.FreqDist(tokens_by_cleaned_split)
freq_by_nltk
import pprint
pprint.pprint(freq_by_nltk)

import operator
sorted_freq_by_nltk=sorted(freq_by_nltk.items(), key=operator.itemgetter(1), reverse=True)

pprint.pprint(sorted_freq_by_nltk)
freq_by_nltk.plot(30)  # this plots the first 30 frequencies
freq_by_nltk.plot(30,cumulative=True)

import re
import nltk
tokens=re.split(' ',"Mark is studying in Centennial College in Toronto")
print(tokens)
tagged=nltk.pos_tag(tokens)
print (tagged)


