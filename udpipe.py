import spacy_udpipe
import pandas as pd
from pprint import pprint
import pickle
spacy_udpipe.download("en") # download English model
nlp = spacy_udpipe.load("en")


#text = "Wikipedia is a free online encyclopedia, created and edited by volunteers around the world. Das ist ein zweiter Satz."
#doc = nlp(text)
#sentences = [sent.string.strip() for sent in doc.sents]
#print(sentences)



# with open('../bert_final/reviews_as_raw_text.txt') as fopen:
#     reviews = fopen.read().split('\n')[:-1]
# #print(reviews)
# df = pd.DataFrame({"review_text":reviews})
#
# #print(df)
#
# testliste = []
# testliste2 = []
# for index, review in enumerate(df["review_text"]):
#     rev_doc = nlp(review)
#     testliste2 = ([sent.string.strip() for sent in rev_doc.sents])
#     #print(testliste2)
#     testliste.append(testliste2)
# pprint(testliste)

# with open('outfile', 'wb') as fp:
#     pickle.dump(testliste, fp)

with open ('outfile', 'rb') as fp:
     itemlist = pickle.load(fp)
#
# pprint(itemlist[:4])


testlist = []
temp = []
for index, review in enumerate(itemlist[:2]):
    #print("first", index, review)
    for index2,r in enumerate(review):
        #print("2nd", index2)
        print(index, index2,r)
        temp=[index+1,index2+1,r]
        testlist.append(temp)
df = pd.DataFrame(testlist,columns=["review_no", "phrase_no", "phrase"])
pprint(df)