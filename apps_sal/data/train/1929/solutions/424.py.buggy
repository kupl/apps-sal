class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:
    
    def __init__(self, words: List[str]):
    
        self.root = TrieNode()

        self.letterlist = \"\"

        for word in words:
            self._insert_word(word)
    
    def _insert_word(self, word):
        node = self.root
        
        for c in word[::-1]:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True    

    def query(self, letter: str) -> bool:
        self.letterlist += letter
        node = self.root
        k = 0
        
        for c in self.letterlist[::-1]:
            k += 1
            if c not in node.children:
                return False
            node=node.children[c]
            if k > 0 and node.is_word:
                return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
