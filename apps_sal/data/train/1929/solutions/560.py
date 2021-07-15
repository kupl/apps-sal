class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
        
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
        return TrieNode() 
  
    def _charToIndex(self,ch): 
        return ord(ch)-ord('a')
    
    
    def insert(self,key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
  
        pCrawl.isEndOfWord = True
    
    def search(self, key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return 0
            pCrawl = pCrawl.children[index]
        if pCrawl != None and pCrawl.isEndOfWord:
            return 1
        if pCrawl != None:
            return 2
        return 0
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        # self.firsts = set()
        # self.lasts = set()
        # self.tots = set()
        for word in words:
            self.root.insert(word[::-1])
            # self.tots.add(word)
            # self.firsts.add(word[0])
            # self.lasts.add(word[-1])
        self.streams = []
        self.l = 0

    def query(self, letter: str) -> bool:
        self.streams.append(letter)
        self.l+=1
        # if letter not in self.lasts:
        #     return False
        for i in range(self.l,-1,-1):
            word = list(reversed(self.streams[i:self.l]))
            # print (word)
            if word == []:
                continue
            k = self.root.search(word)
            if k == 1:
                return True
            if k == 0:
                break

        return False
                
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

