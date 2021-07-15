class TrieNode:    
    def __init__(self):
        self.children = {}
        self.is_leaf = False
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.root = self.trie
        self.buf = []
        
        for word in words:
            self.trie = self.root
            for i in range(len(word)-1, -1, -1):
                ch = word[i]
                if ch not in self.trie.children:
                    self.trie.children[ch] = TrieNode()
                self.trie = self.trie.children[ch]
            self.trie.is_leaf = True
        

    def query(self, letter: str) -> bool:
        self.buf.append(letter)
        self.trie = self.root
        for i in range(len(self.buf)-1,-1,-1):            
            if self.buf[i] in self.trie.children:
                self.trie = self.trie.children[self.buf[i]]
                if self.trie and self.trie.is_leaf:
                    return True
            else:
                return False

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

