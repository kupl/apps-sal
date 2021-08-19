class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.start = []

        for word in words:
            self.add(word)

    def add(self, word):
        curr = self.trie

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = True

    def query(self, letter: str) -> bool:

        start = []
        if letter in self.trie:
            start.append(self.trie[letter])

        for p in self.start:
            if letter in p:
                start.append(p[letter])

        self.start = start

        return any('#' in p for p in self.start)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
