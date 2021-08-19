class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            lastC = self.trie
            for c in w:
                lastC[c] = lastC.get(c, {})
                lastC = lastC[c]
            lastC['*'] = True
        self.words = []

    def query(self, letter: str) -> bool:
        newWords = []
        if letter in self.trie:
            newWords.append(self.trie[letter])
        for t in self.words:
            if letter in t:
                newWords.append(t[letter])
        self.words = newWords
        return any(['*' in t for t in self.words])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
