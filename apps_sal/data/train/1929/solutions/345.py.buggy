class TrieNode:
    def __init__(self):
        self.edges={}
    
    def get_edge(self,edge):
        return self.edges[edge]
    
    def add_edge(self,edge):
        if not self.has_edge(edge):
            self.edges[edge]=TrieNode()
            
    def has_edge(self,edge):
        return edge in self.edges
    
    def isWord(self):
        return \"$\" in self.edges
    
class Trie:
    
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        cur=self.root
        for c in word:
            cur.add_edge(c)
            cur=cur.get_edge(c)
        cur.add_edge(\"$\")
        
    def search(self, word):
        cur=self.root
        for c in word:
            if cur.isWord():
                return True
            if not cur.has_edge(c):
                return False
            cur=cur.get_edge(c)
        return cur.isWord()
from collections import deque
class StreamChecker:
    def __init__(self, W):
        self.prefix=deque()
        self.trie=Trie()
        for w in W:
            self.trie.insert(w[::-1])

    def query(self, c):
        self.prefix.appendleft(c)
        return self.trie.search(self.prefix)


\"\"\"
time:  9:00AM
Try defaultdict as well 

\"\"\"
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
