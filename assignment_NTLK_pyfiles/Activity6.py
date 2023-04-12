import re
import nltk
tokens=re.split(' ',"Mark is studying in Centennial College in Toronto")
print(tokens)
tagged=nltk.pos_tag(tokens)
print (tagged)

entities = nltk.chunk.ne_chunk(tagged)
print (entities)

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
