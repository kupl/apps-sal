#
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie(): 
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word): 
        node = self.root 
        for char in word: 
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.currquery = \"\"
        self.trie = Trie()
        for word in words: 
            self.trie.insert(word[::-1])
    
    def query(self, letter: str) -> bool:
        self.currquery += letter
        node = self.trie.root
        for i in self.currquery[::-1]: 
            if i not in node.children: 
                return False
            else: 
                node = node.children[i]
                if node.isEnd:
                    return True
                
                
    

