class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            d = self.trie
            for c in w:
                if c in d:
                    d = d[c]
                else:
                    d[c] = {}
                    d = d[c]
            d['$'] = None
        self.l = []

    def query(self, letter: str) -> bool:
        self.l = [j[letter] for j in self.l if letter in j]
        if letter in self.trie:
            self.l.append(self.trie[letter])
        return any(['$' in i for i in self.l])
