from nltk.stem import PorterStemmer
from math import log10
import re
import os
from collections import defaultdict
import json

CORPUS = "/Users/vincentngo/Desktop/121M2/search/database"
#This should be a path to a folder for the corpus that is locally available

DOC_IDS = "/Users/vincentngo/Desktop/121M2/search/database/docMappingTest.json"
#This should be a path to a file, containing a dicotionary of all the doc IDs

CORPUS_FILES = list()

IDS_DOCUMENT = None

for filename in os.listdir(CORPUS):
    CORPUS_FILES.append(filename)
#Gets a list of the different data files containing the reverse indexes

with open(DOC_IDS, 'r') as f:
    IDS_DOCUMENT = json.load(f)

def stem_word(word: str):
#Uses the Porter Stemming Algorithm to stem each word
    porterStemmer = PorterStemmer()
    return porterStemmer.stem(word)

def tokenize(text):
#Takes in a string and seperates each word, ignores punctuations
    return re.findall(r'\b\w+\b', text.lower())

def search(query: str):
    #Tokenizes and Stems each word of the Query
    query_tokens = tokenize(query)
    stemmed_tokens = [stem_word(token) for token in query_tokens]
    parse_list = list()
    #Iterates through the tokens and finds the necessary corpus files to run through based on alphabatization
    for tokens in stemmed_tokens:
        if tokens[0:2].isalnum():
            if len(tokens) >= 2:
                parse_list.append(f"{CORPUS}/{tokens[0:2]}.json")
            else: 
                parse_list.append(f"{CORPUS}/{tokens[0]*2}.json")
        else:   
            parse_list.append(f"{CORPUS}/!.json")
    count = 0

    #Copying the data of the query, which will include all of the docs with the structure 
    #[(ID, TF-IDF SCORE, IMPORTANT/NOT),...]
    result = list()
    for file in parse_list:
        with open(file, 'r') as f:
            document = json.load(f)
            if stemmed_tokens[count] in document.keys():
                result.append(document[stemmed_tokens[count]])
    returned_list = result[0]

    #Computes the combined scores of multiword queries
    for w in range(len(result) - 1):
        i = 0
        j = 0
        computing_list = list()
        while (i <= len(returned_list) and j <= len(result[w+1])):
            if returned_list[0] == result[w+1][j][0]:
                computing_list.append([returned_list[0], returned_list[1] + result[w+1][j][1], returned_list[2] | result[w+1][j][2]])
                i += 1
                j += 1
            elif returned_list[0] < result[w+1][j][0]:
                i += 1
            else:
                j += 1
        returned_list = computing_list

    #Sort by TF-IDF SCORES and IMPORTANT WORDS
    returned_list.sort(key=lambda x: x[1]+x[2], reverse=True)
    return [IDS_DOCUMENT, returned_list[0:10]]

def main():
    #A seperate main function to accept user input into the search function
    user_input = input("Please Enter a Query: ")
    search(user_input)

if __name__ == "__main__":
    #Used for testing and running the search function.
    main()

        
    

