class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.d = collections.defaultdict(set)
        for word in words:
            self.d[word[-1]].add(word)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any((self.s.endswith(w) for w in self.d[letter]))
