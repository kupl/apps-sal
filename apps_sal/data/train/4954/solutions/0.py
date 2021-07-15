import re
class WordDictionary:
    def __init__(self):
        self.data=[]
  
    def add_word(self,x):
        self.data.append(x)
  
    def search(self,x):
        for word in self.data:
            if re.match(x+"\Z",word): return True
        return False
