class Trie:
    
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add(self, word: str):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.isWord = True
    
    def contains(self, prefix: str):
        cur = self
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
            if cur.isWord:
                return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.prefix = \"\"
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])

    def query(self, letter: str) -> bool:
        self.prefix += letter
        return self.trie.contains(self.prefix[::-1])
    
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
