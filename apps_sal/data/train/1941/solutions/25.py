class Solution:
    def findNumOfValidWords(self, words, puzzles):
        count = collections.Counter(frozenset(w) for w in words)
        res = []
        for p in puzzles:
            cur = 0
            for k in range(7):
                for c in itertools.combinations(p[1:], k):
                    # print(c)
                    cur += count[frozenset(tuple(p[0]) + c)]
            res.append(cur)
        return res
