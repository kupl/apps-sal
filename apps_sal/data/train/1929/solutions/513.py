class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.d = collections.defaultdict(set)
        for w in words:
            self.d[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any((self.s.endswith(w) for w in self.d[letter]))
