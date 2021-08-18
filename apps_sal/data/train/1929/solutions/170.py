class TN:
    def __init__(self, eow=False):
        self.c = {}
        self.e = eow
        self.i = id(self)

    def add(self, s):
        if len(s) == 0:
            self.e = True
        else:
            c = s[0]
            if c not in self.c:
                self.c[c] = TN()
            self.c[c].add(s[1:])

    def search(self, w):
        t = self
        for c in w:
            if c not in t.c:
                return False
            else:
                t = t.c[c]
                if t.e:
                    return True
        return False

    def __contains__(self, i):
        return i in self.c

    def p(self, s=0):
        for k, v in self.c.items():
            print(' ' * s, k, '*' if v.e else '', sep='')
            v.p(s + 1)

    def __str__(self):
        return str(self.c) + ('*'if self.e else '')

    def __repr__(self):
        return repr(self.c) + ('*'if self.e else '')


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TN()
        for w in words:
            self.root.add(w[::-1])
        self.s = []

    def query(self, letter: str) -> bool:
        self.s.append(letter)
        return self.root.search(reversed(self.s))
