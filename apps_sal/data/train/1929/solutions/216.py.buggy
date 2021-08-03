class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True
    
    def find(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_word:
                return True
        return False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.history = \"\"
        for word in words:
            self.trie.insert(word[::-1])
        

    def query(self, letter: str) -> bool:
        self.history = letter + self.history
        return self.trie.find(self.history)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
