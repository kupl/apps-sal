class StreamChecker:

    def __init__(self, words: List[str]):
        self.d = {}
        for w in words:
            cur = self.d
            for c in w:
                cur.setdefault(c, dict())
                cur = cur[c]
            cur[''] = True
        self.q = []

    def query(self, letter: str) -> bool:
        nq = []
        if letter in self.d:
            nq += [self.d[letter]]
        for pq in self.q:
            if letter in pq:
                nq += [pq[letter]]
        self.q = nq
        for qq in self.q:
            if '' in qq:
                return True
        return False
