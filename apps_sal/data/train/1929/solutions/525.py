class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.di = collections.defaultdict(set)
        for w in words:
            self.di[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any((self.s.endswith(w) for w in self.di[letter]))
