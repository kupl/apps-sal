class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words = [frozenset(word) for word in words if len(set(word)) <= 7]
        counter = Counter(words)
        res = []
        for p in puzzles:
            pre = (p[0],)
            t = set(p[1:])
            tmp = 0
            for i in range(len(t) + 1):
                for c in itertools.combinations(t, i):
                    tmp += counter[frozenset(pre + c)]
            res += [tmp]
        return res
