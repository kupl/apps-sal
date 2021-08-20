class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.check = []
        for w in words:
            d = self.trie
            for c in w:
                _d = d.get(c, {})
                d[c] = _d
                d = _d
            d['.'] = True
        print(self.trie)

    def query(self, letter: str) -> bool:
        next_check = []
        found = False
        for d in self.check + [self.trie]:
            if letter in d:
                _d = d[letter]
                if '.' in _d:
                    found = True
                next_check.append(_d)
        self.check = next_check
        return found
