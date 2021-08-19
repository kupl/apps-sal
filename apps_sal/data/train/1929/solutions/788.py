class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = set()
        for w in words:
            self.s = self.s.union(set(w))
        self.d = {}
        for w in words:
            insert(self.d, w)
        self.l = []
        # print(self.d)

    def query(self, letter: str) -> bool:
        if letter not in self.s:
            return False
        d = self.d
        l = self.l
        b = False
        for i in reversed(list(range(len(l)))):
            if letter in l[i]:
                l[i] = l[i][letter]
                if '#' in l[i]:
                    b = True
            else:
                del l[i]
        if letter in d:
            l.append(d[letter])
            if '#' in l[-1]:
                b = True
        return b


def insert(d, s):
    if len(s) == 0:
        d['#'] = {}
    else:
        if s[0] not in d:
            d[s[0]] = {}
        insert(d[s[0]], s[1:])

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
