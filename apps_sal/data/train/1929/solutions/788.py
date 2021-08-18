class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = set()
        for w in words:
            self.s = self.s.union(set(w))
        self.d = {}
        for w in words:
            insert(self.d, w)
        self.l = []

    def query(self, letter: str) -> bool:
        if letter not in self.s:
            return False
        d = self.d
        l = self.l
        b = False
        for i in reversed(list(range(len(l)))):
            if letter in l[i]:
                l[i] = l[i][letter]
                if '
                    b = True
            else:
                del l[i]
        if letter in d:
            l.append(d[letter])
            if '
                b = True
        return b


def insert(d, s):
    if len(s) == 0:
        d['
    else:
        if s[0] not in d:
            d[s[0]] = {}
        insert(d[s[0]], s[1:])
