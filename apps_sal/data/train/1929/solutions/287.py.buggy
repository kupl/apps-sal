class TrieNode:
    
    def __init__(self):
        self.child = {}
        self.end = False
    
    def insert(self, word):
        node = self
        idx = 0
        for char in word:
            if node.child.get(char) is None:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.end = True
    
    def search(self, word):
        node = self
        for char in word:
            if node.child.get(char) is None:
                return False
            node = node.child[char]
            if node.end:
                return True
        return False
        
                
        

class StreamChecker:

    def __init__(self, words: List[str]):
        self.maxLen = max(map(len, words))
        self.trie = TrieNode()
        for word in words:
            self.trie.insert(\"\".join(list(word)[::-1]))
        self.curQuery = ''

    def query(self, letter: str) -> bool:
        self.curQuery = letter + self.curQuery[:min(len(self.curQuery), self.maxLen - 1)]
        return self.trie.search(self.curQuery)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
