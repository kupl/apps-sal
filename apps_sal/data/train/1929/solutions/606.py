class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = {}
        self.history = ''
        for w in words:
            p = self.trie
            for c in w[::-1]:
                if c not in p: p[c] = {}
                p = p[c]
            p['#'] = ''

    def query(self, letter: str) -> bool:
        self.history+=letter
        p = self.trie
        for c in self.history[::-1]:
            if c not in p: return False
            p = p[c]
            if '#' in p: return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

