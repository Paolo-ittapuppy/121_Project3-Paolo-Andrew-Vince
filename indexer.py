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
from string import ascii_lowercase
import re
from urllib.parse import urlparse

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
    storeDocMap(docMapDB+str(dbCount)+'.db', maping)

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
    if not is_valid(data["url"]):
        return

    #do i need to make sure the document is valid like in project2? im confused
    webPage = BeautifulSoup(data["content"], "html.parser")
    words = tokenizer.tokenize(webPage.text)
    freq = tokenizer.computeWordFrequencies(words, ps)

    #too little words in doc
    if len(words) < 20:
        return
    #too much repitition
    if (len(freq.keys())+1)/(len(words)+1) <= float(.2):
        return
    #duplication check needs to be done

    map[id] = data["url"]
    for word, f in freq.items():
        index[word].append((id, f))

#recursive combining of all the db files to create the one large reverse index that still needs to be partitioned for queires
def combineReverseIndexes(path, folderNumber):
    counter = 1
    name = 1
    while(os.path.isfile(path + str(folderNumber) +'\RI' + str(counter+1) +'.db')):
        print(path+ str(folderNumber)+'\RI' + str(counter+1) +'.db')
        f1 = open(path+ str(folderNumber)+'\RI' + str(counter) +'.db', 'r')
        f2 = open(path+ str(folderNumber)+'\RI' + str(counter+1) +'.db', 'r')
        json1 = json.load(f1)
        json2 = json.load(f2)
        f1.close()
        f2.close()
        json3 = {}
        for key in json1.keys():
            if key in json2:
                json3[key] = json1[key] + json2[key]
                del json2[key]
            else:
                json3[key] = json1[key]
        json3.update(json2)
        f3 = open(path + str(folderNumber+1)+ '\RI' + str(name) + '.db', 'w')
        json.dump(json3, f3)
        f3.close
        counter += 2
        name += 1

    if name == 1:
        return
    if os.path.isfile(path + str(folderNumber) +'\RI' + str(counter) +'.db'):
        f1 = open(path+ str(folderNumber)+'\RI' + str(counter) +'.db', 'r')
        json1 = json.load(f1)
        f1.close()
        f3 = open(path + str(folderNumber+1)+ '\RI' + str(name) + '.db', 'w')
        json.dump(json1, f3)
        f3.close
    #combineReverseIndexes(path, folderNumber+1)

def wordCounter(path):
    counter = 1
    wordCount = 0
    while(os.path.isfile(path+'\RI' + str(counter) +'.db')):
        #print(path+'\RI' + str(counter) +'.db')
        f1 = open(path+'\RI' + str(counter) +'.db', 'r')
        j = json.load(f1)
        f1.close()
        wordCount += len(j)
        print(wordCount)
        counter += 1
    print(wordCount, 'final')

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        
        if not re.match(r".*(.ics.uci.edu/|.ics.uci.edu/|.informatics.uci.edu/|.stat.uci.edu/|)", parsed.netloc):
            return False

        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise



if __name__ == "__main__":
    '''
    i = input()
    print('start')
    reverseIndex(i, "RI", "docMap")
    '''
    combineReverseIndexes(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesTest', 6)



    