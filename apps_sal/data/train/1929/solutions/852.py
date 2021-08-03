class StreamChecker:

    def __init__(self, words: List[str]):
        self.d = {}
        for w in words:
            c = self.d
            i = 0
            while i < len(w):
                if w[i] not in c:
                    c[w[i]] = {}
                c = c[w[i]]
                i += 1
            c[''] = True
        self.ps = []

    def query(self, letter: str) -> bool:
        nps = []
        for p in self.ps + [self.d]:
            if letter in p:
                nps.append(p[letter])
        self.ps = nps
        return any('' in p for p in self.ps)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
