
#class to represent a words appearance in a document
class Posting():
    
    def __init__(self, word, id, occurance):
        self.word = word #maybe get rid of
        self.id = id
        self.occurance = occurance

    def id(self):
        return self.id
    
    def occurance(self):
        return self.occurance