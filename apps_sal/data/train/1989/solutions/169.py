class Solution:

    def __init__(self):
        self.mn = {}
        self.mx = {}

    def calcMax(self, tuple1, tuple2):
        ret = 0
        if tuple1 not in self.mn or tuple2 not in self.mn:
            return 0
        ret = max(abs(self.mn[tuple1] - self.mn[tuple2]), ret)
        ret = max(abs(self.mn[tuple1] - self.mx[tuple2]), ret)
        ret = max(abs(self.mx[tuple1] - self.mn[tuple2]), ret)
        ret = max(abs(self.mx[tuple1] - self.mx[tuple2]), ret)
        return ret

    def longestAwesome(self, s: str) -> int:
        l = len(s)
        curTup = [False, False, False, False, False, False, False, False, False, False]
        self.mn[tuple(curTup)] = 0
        self.mx[tuple(curTup)] = 0
        for i in range(l):
            curInt = int(s[i])
            curTup[curInt] = not curTup[curInt]
            if tuple(curTup) not in self.mn:
                self.mn[tuple(curTup)] = i + 1
            self.mx[tuple(curTup)] = i + 1
        mx = 0
        for tup in list(self.mx.keys()):
            mx = max(mx, self.calcMax(tup, tup))
            tupList = []
            for i in tup:
                tupList.append(i)
            for i in range(len(tupList)):
                tupList[i] = not tupList[i]
                mx = max(mx, self.calcMax(tup, tuple(tupList)))
                tupList[i] = not tupList[i]
        return mx
