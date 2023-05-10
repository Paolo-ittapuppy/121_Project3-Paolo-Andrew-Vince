import sqlite3
import json
from bs4 import BeautifulSoup
import pathlib
import os
from collections import defaultdict
#idea: go through some number of files, start indexing words to websties, transition that into a sqlite format, then restart
#dictionary, and keep going. 

def reverseIndex(dir:str, RIndDB:str, docMapDB:str):
    counter = 0
    maxCounter = 300
    index = defaultdict(list)
    maping = {}
    currentID = 1
    #format of reverse index: {word:[()]}
    for path in os.listdir(dir):
        for file in os.listdir(path):
            counter +=1 
            readHTML(file, index)
            if counter >= maxCounter:
                storeIndexes(RIndDB, index)
                storeDocMap(docMapDB, maping)
            currentID +=1
            pass

        storeIndexes()
        #reset data


def storeIndexes(file, data):
    #test
    pass

def storeDocMap(file, data):
    #test
    pass

def readHTML(path, index):
    #update the index, adding the path to the list of the words key
    pass
    