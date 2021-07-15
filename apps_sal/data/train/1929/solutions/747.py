class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        
        node.last = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
            
            if node.last:
                return True
        
        return False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        
        self.letters = \"\"
        

    def query(self, letter: str) -> bool:
        
        self.letters += letter
        word_to_search = self.letters[::-1]
        
        # print(word_to_search)
        return self.trie.search(word_to_search)
        
        
        
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
