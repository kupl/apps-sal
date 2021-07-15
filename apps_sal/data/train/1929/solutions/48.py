class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.possible = []
        for word in words:
            t = self.trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'

    def query(self, letter: str) -> bool:
        temp = []
        if letter in self.trie:
            temp.append(self.trie[letter])
        for d in self.possible:
            if letter in d:
                temp.append(d[letter])
        self.possible = temp
        return any('#' in item for item in self.possible)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

