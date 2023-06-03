import indexer
import Alphebetize
import os

i = input()
print('start')
indexer.reverseIndex(i, "ReverseIndexesFolder1\RI", "docMap")
print('indexed all documents')
print('combining:')
indexer.combineReverseIndexes(os.getcwd() +r'\\ReverseIndexesFolder', 1)
indexer.combineReverseIndexes(os.getcwd() +r'\\ReverseIndexesFolder', 2)
indexer.combineReverseIndexes(os.getcwd() + r'\\ReverseIndexesFolder', 3)
indexer.combineReverseIndexes(os.getcwd() +r'\\ReverseIndexesFolder', 4)
indexer.combineReverseIndexes(os.getcwd() + r'\\ReverseIndexesFolder', 5)
indexer.combineReverseIndexes(os.getcwd() + r'\\ReverseIndexesFolder', 6)
print('combining done')

print('splitting jsons into alphabet')
Alphebetize.combineIds(os.getcwd() + r'\\docMaps\\', os.getcwd() +r'\\docMappingTest.json')
Alphebetize.splitLargeJson(os.getcwd() + r"\\ReverseIndexesFolder7\RI1.json", os.getcwd() +r'\\alpha\\', 55393) 
Alphebetize.splitingAlpha(os.getcwd() +r'\\alpha\\', os.getcwd()+ r'\\AlphaAlpha\\')

print('done')