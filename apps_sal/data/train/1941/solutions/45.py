class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        count = collections.Counter(frozenset(w) for w in words)
        res = []
        for p in puzzles:
            subs = [p[0]]
            for c in p[1:]:
                subs += [s + c for s in subs]
            res.append(sum(count[frozenset(s)] for s in subs))
        return res
