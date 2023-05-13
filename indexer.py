import sqlite3
import json
from bs4 import BeautifulSoup
import pathlib
import os
from collections import defaultdict
import posting
import tokenizer
from sys import getsizeof
from nltk.stem import PorterStemmer

#idea: go through some number of files, start indexing words to websties, transition that into a sqlite format, then restart
#dictionary, and keep going. 

#creates a reverse index given a path w/ directories with all the files, lowkey this should be recursive but im dizzy thinking about that
def reverseIndex(dir:str, RIndDB:str, docMapDB:str):
    ps = PorterStemmer()
    counter = 0
    maxCounter = 1000
    index = defaultdict(list)
    maping = {}
    currentID = 1
    dbCount = 1
    #format of reverse index: {word:[()]}
    for root, dir, files in os.walk(dir):
        f = [os.path.join(root, i) for i in files]
        for file in f:
            counter +=1
            if(counter%200 == 0):
                print(counter) 
            readHTML(file, index, currentID, ps, maping)
            if counter >= maxCounter: #change to be when index is too big
                storeIndexes(RIndDB+str(dbCount)+'.db', index)
                index = defaultdict(list)
                storeDocMap(docMapDB+str(dbCount)+'.db', maping)
                maping = {}
                dbCount +=1
                counter = 0
            currentID +=1

    storeIndexes(RIndDB+str(dbCount)+'.db', index)


def storeIndexes(file, data):
    f = open(file, 'w')
    j = json.dump(data, f)
    f.close()
    pass

def storeDocMap(file, data):
    #test
    f = open(file, 'w')
    j = json.dump(data, f)
    f.close()
    pass

def readHTML(path, index, id, ps, map):
    #print(path)
    file = open(path, 'r')
    data = json.load(file)
    file.close()
    map[id] = data["url"]
    #do i need to make sure the document is valid like in project2? im confused
    webPage = BeautifulSoup(data["content"], "html.parser")
    words = tokenizer.tokenize(webPage.text)
    freq = tokenizer.computeWordFrequencies(words, ps)
    for word, f in freq.items():
        index[word].append((word, id, f))


if __name__ == "__main__":
    i = input()
    print('start')
    reverseIndex(i, "RI", "docMap")

    