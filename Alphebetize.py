import string
alphabet = list(string.ascii_lowercase)
import ijson
from collections import defaultdict
import json
import os

#split large json file with all the data combined into smaller alphabetizxed files for easier qeuery search
def splitLargeJson(path, pathToWrite): 
    letterToFile = {}
    jsonHolder = defaultdict(dict)
    #create all 27 files and 27 dictionaires to store the json data
    for letter in alphabet:
        letterToFile[letter] = open(pathToWrite + letter + '.db', 'w')
        jsonHolder[letter] = {}
    letterToFile['!'] = open(pathToWrite + '\!.db','w' )
    jsonHolder['!'] = {}

    #iteravly search through the json file
    with open(path, 'rb') as f:
        for k, v in ijson.kvitems(f, ""):
            print(k)
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

def combineIds(folder, fileToWriteTo):
    d = {}
    for f in os.listdir(folder):
        with open(folder + f, 'r') as file:
            d.update(json.load(file))
    with open(fileToWriteTo, 'w') as f:
        json.dump(sorted(d), f)

if __name__ == "__main__":
    combineIds(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\docMaps\\', r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\docMappingTest.db')
    #splitLargeJson(r"C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\RI1.db", r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\alpha\\') 