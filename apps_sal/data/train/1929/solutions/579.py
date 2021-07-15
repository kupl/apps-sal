from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.is_end=False


class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,s):
        tem=self.root
        for i in s:
            tem=tem.children[i]
        tem.is_end=True
        
    def search(self,s):
        tem=self.root
        for i in range(len(s)):
            node=tem.children.get(s[i])
            if(node==None):
                return False
            if(node.is_end):
                return True
            
            tem=node
            
        return tem.is_end
        


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie=Trie()
        self.ls=words
        for i in self.ls:
            self.trie.insert(i[::-1])
        self.q=\"\"
        

    def query(self, letter: str) -> bool:
        self.q+=letter
        return self.trie.search(self.q[::-1])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
