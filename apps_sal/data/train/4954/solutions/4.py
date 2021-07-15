import re
class WordDictionary:
    def __init__(self):
       self.words = []
    
    def add_word(self,v):
       self.words.append(v)
  
    def search(self,rg):
        return any(re.match(r'^{}$'.format(rg),i) for i in self.words)
