class StreamChecker:

    def __init__(self, words: List[str]):
        dic = {}
        for w in words:
            p = dic
            for c in w:
                if c not in p: p[c] = {}
                p = p[c]
            p['#'] = True
        self.dic = dic
        self.cur = []

    def query(self, letter: str) -> bool:
        tmp, self.cur = self.cur, []
        tmp.append(self.dic)
        res = False
        for d in tmp:
            if letter in d:
                self.cur.append(d[letter])
                if '#' in d[letter]:
                    res = True
        return res

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

