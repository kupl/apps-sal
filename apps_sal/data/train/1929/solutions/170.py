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
            # print(c,t)
            if c not in t.c:
                # print('oops', t.c)
                return False
            else:
                t = t.c[c]
                if t.e:
                    return True
        # print('nope')
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
        # self.root.p()
        # self.av = set()

    def query(self, letter: str) -> bool:
        self.s.append(letter)
        return self.root.search(reversed(self.s))
        # found = False
        # print(self.av, letter)
        # for n in list(self.av):
        #     if letter in n:
        #         self.av.remove(n)
        #         self.av.add(n.c[letter])
        #         found = found or n.c[letter].e
        #     else:
        #         self.av.remove(n)
        # if letter in self.root:
        #     print('found',self.root.c[letter])
        #     self.av.add(self.root.c[letter])
        #     found = found or self.root.c[letter].e
        # print(found)
        # return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
