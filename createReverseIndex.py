import indexer
import Alphebetize

i = input()
print('start')
indexer.reverseIndex(i, "ReverseIndexesFolder1\RI", "docMap")

indexer.combineReverseIndexes(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder', 1)
indexer.combineReverseIndexes(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder', 2)
indexer.combineReverseIndexes(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder', 3)
indexer.combineReverseIndexes(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder', 4)
indexer.combineReverseIndexes(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder', 5)
indexer.combineReverseIndexes(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder', 6)

Alphebetize.combineIds(r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\docMaps\\', r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\docMappingTest.json')
Alphebetize.splitLargeJson(r"C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\ReverseIndexesFolder7\RI1.json", r'C:\Users\Urani\cs 121\121_Project3-Paolo-Andrew-Vince\alpha\\', 55393) 