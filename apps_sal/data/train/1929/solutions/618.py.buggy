class Trie:
    def __init__(self):
        self.child = {}
        self.isWord = False

    def add(self, s):
        t = self
        for c in s:
            if c not in t.child:
                t.child[c] = Trie()
            t = t.child[c]
        t.isWord = True

    def check(self, s):
        t = self
        for c in s:
            if c not in t.child:
                return False
            t = t.child[c]
            if t.isWord:
                return True
        return t.isWord

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.cache = \"\"
        self.visited = {}
        for s in words:
            self.trie.add(s[::-1])

    def query(self, letter: str) -> bool:
        self.cache = self.cache + letter
        return self.trie.check(self.cache[::-1])
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
