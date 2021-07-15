from re import match

class WordDictionary:
    def __init__(self):
        self.db = []
  
    def add_word(self, word):
        self.db.append(word)
  
    def search(self, word):
        return bool([w for w in self.db if match(rf'^{word}$', w)])
