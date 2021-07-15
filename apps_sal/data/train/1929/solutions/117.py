class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend_word = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isend_word = True
        
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.search = []
        for word in words:
            self.trie.insert(word[::-1])
        
        
    def query(self, letter: str) -> bool: 
        self.search.append(letter)
        curr = self.trie.root
        for i in range(len(self.search) - 1, -1, -1):
            char = self.search[i]
            if curr.isend_word:
                return True
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.isend_word


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

