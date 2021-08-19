class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.p = []
        for w in words:
            self.insert(w)

    def insert(self, w):
        p = self.trie
        for c in w:
            if c in p:
                p = p[c]
            else:
                p[c] = {}
                p = p[c]
        p['#'] = ''

    def query(self, letter: str) -> bool:
        self.p.append(self.trie)
        p2 = []
        for p in self.p:
            if letter in p:
                p2.append(p[letter])
        self.p = p2
        return any('#' in p for p in self.p)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
