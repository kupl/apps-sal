class StreamChecker:

    def __init__(self, words: List[str]):
        self.q = ''
        self.m = defaultdict(set)
        for w in words:
            self.m[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.q += letter
        return any(filter(lambda w: self.q.endswith(w), self.m[letter]))
