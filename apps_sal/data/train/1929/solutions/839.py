class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.history = ''
        self.trie = {}
        for w in words:
            p = self.trie
            for c in w:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['#'] = w
        self.p = [self.trie]

    def query(self, letter: str) -> bool:
        self.history += letter
        self.p = [p[letter] for p in self.p if letter in p]
        res = any(['#' in p for p in self.p])
        self.p += [self.trie]
        return res

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
