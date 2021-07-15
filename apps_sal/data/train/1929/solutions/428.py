from collections import defaultdict as dd
class trieNode :
    def __init__(self) :
        self.children = dd(int)
        self.is_end = False
        
class trie :
    def __init__(self) :
        self.root = trieNode()
        
    def add(self,word) :
        
        par=self.root
        for char in word[::-1] :
            if par.children[char]==0 :
                par.children[char] = trieNode()
            par=par.children[char]
        par.is_end = True
        
    def check(self,s) :
        par=self.root
        for char in s[::-1] :
            if par.children[char] :
                par=par.children[char]
                if par.is_end :
                    return True
            
            else :
                return False
        return False
                
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = trie()
        self.cur = \"\"
        for word in words :
            self.trie.add(word)

    def query(self, letter: str) -> bool:
        self.cur+=letter
        if self.trie.check(self.cur) :
            return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
