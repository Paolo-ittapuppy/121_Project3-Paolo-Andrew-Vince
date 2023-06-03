import string
alphabet = list(string.ascii_lowercase)
numbers = ['0','1','2','3','4','5','6','7','8','9']
import ijson
from collections import defaultdict
import json
import os
import math

#split large json file with all the data combined into smaller alphabetizxed files for easier qeuery search
def splitLargeJson(path, pathToWrite, total): 
    letterToFile = {}
    jsonHolder = defaultdict(dict)
    #create all 27 files and 27 dictionaires to store the json data
    for letter in alphabet:
        letterToFile[letter] = open(pathToWrite + letter + '.json', 'w')
        jsonHolder[letter] = {}
    letterToFile['!'] = open(pathToWrite + '\!.json','w' )
    jsonHolder['!'] = {}

    #iteravly search through the json file
    with open(path, 'rb') as f:
        for k, v in ijson.kvitems(f, ""):
            totalOc = len(v)
            for docAppearance in v:
                docAppearance[1] = calcTfIdf(docAppearance[1], total, totalOc)
            if k[0] in alphabet:
                jsonHolder[k[0]][k] = v
            else:
                jsonHolder['!'][k] = v
    
    for k, v in jsonHolder.items():
        if k in alphabet:
            json.dump(jsonHolder[k], letterToFile[k])
            letterToFile[k].close()
        else:
            json.dump(jsonHolder['!'], letterToFile['!'])
            letterToFile['!'].close()

def calcTfIdf(tf, corp, totalOc):
    return round(float(tf) * float(math.log(corp/totalOc)), 4)

def combineIds(folder, fileToWriteTo):
    d = {}
    for f in os.listdir(folder):
        print(folder + f)
        with open(folder + f, 'r') as file:
            d.update(json.load(file))
    print(d)
    with open(fileToWriteTo, 'w') as f:
        json.dump(d, f)

def splitingAlpha(folder, folderToWriteTo):
    newJsons = defaultdict(dict)
    letterToFile = {}

    for letter in alphabet:
        for letter2 in alphabet:
            letterToFile[letter+letter2] = open(folderToWriteTo + letter + letter2 +'.json', 'w')
            newJsons[letter + letter2] = {}
    for letter in alphabet:
        letterToFile[letter+'!'] = open(folderToWriteTo + letter + '!' +'.json', 'w')
        newJsons[letter + '!'] = {}
        for num in numbers:
            letterToFile[letter+num] = open(folderToWriteTo + letter + num +'.json', 'w')
            newJsons[letter + num] = {}

    for num in numbers:
        letterToFile[num+'!'] = open(folderToWriteTo + num + '!' +'.json', 'w')
        newJsons[num + '!'] = {}
        for num2 in numbers:
            letterToFile[num+num2] = open(folderToWriteTo + num + num2 +'.json', 'w')
            newJsons[num + num2] = {}

    letterToFile['!'] = open(folderToWriteTo + '\!.json','w' )
    newJsons['!'] = {}

    for letter in alphabet:
        with open(folder + letter+ '.json', 'r')as file:
            for k, v in ijson.kvitems(file, ""):
                if len(k) >= 2:
                    if k[0] in alphabet and (k[1] in alphabet or k[1] in numbers):
                        newJsons[k[0:2]][k] = v
                    else:
                        newJsons[k[0]+'!'][k] = v
                elif len(k) == 1:
                    newJsons[k[0]*2][k] = v
    
    with open(folder+ '!.json', 'r')as file:
        for k, v in ijson.kvitems(file, ""):
            if len(k) >= 2:
                if k[0] in numbers and k[1] in numbers:
                    newJsons[k[0:2]][k] = v
                else:
                    newJsons['!'][k] = v
            else:
                newJsons['!'][k] = v

    
    for k, v in newJsons.items():
        for _ in v.values():
            for showing in _:
                showing[1] = float(showing[1])
        print(k)
        json.dump(newJsons[k], letterToFile[k])
        letterToFile[k].close()
    
    

if __name__ == "__main__":
    #combineIds(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\docMaps\\', r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\docMappingTest.json')
    #splitLargeJson(r"C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder7\RI1.json", r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\alpha\\', 55393) 
    splitingAlpha(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\alpha\\', r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\AlphaAlpha\\')

