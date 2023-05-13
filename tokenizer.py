import os
import re
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
stop_words = set(stopwords.words('english'))
punctuations = [
    ",",
    ".",
    ":",
    "(",
    ")",
    "$",
    "&",
    "|",
    "�",
    "}",
    "{",
    ";",
    "[",
    "?",
    "]",
    "*",
    "''",
    "@",
    "#",
    "’",
    "!",
    ">",
    "%",
    "<",
    "“",
    "”",
    "=",
    "'",
    "`",
    "��",
    "``",
    "�",
    "-",
    "�"

]
for p in punctuations:
    stop_words.add(p)
#code gotten from "https://www.geeksforgeeks.org/removing-stop-words-nltk-python/"


def tokenize(Text):
    #check if file exists
    tokenList = []
    for t in word_tokenize(Text):
        if t.lower() not in stop_words:
            tokenList.append(t)
    return tokenList
    
def computeWordFrequencies(tokenList, ps):
    #need way to look at bolded words
    tokenMap = {}
    if type(tokenList) == list:
        for word in tokenList:
            tokenMap[ps.stem(word)] = tokenMap.get(ps.stem(word), 0) + 1
    return dict(sorted(tokenMap.items(), key=lambda x:x[1], reverse=True))

#simple O(N) loop through every item in the dictionary oncee. 
def printD(map):
    if type(map) == dict:
        for key, value in map.items():
            print(f"{key} - {value}")

#in total around n^3 time maybe like (nlogn)^3 not completely sure
if __name__ == '__main__':
    file = sys.argv[1]
    printD(computeWordFrequencies(tokenize(file)))