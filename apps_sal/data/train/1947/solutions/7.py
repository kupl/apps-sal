class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        if len(B) == 0:
            return A

        from collections import Counter

        cb = Counter()
        for b in B:
            for char in b:
                cb[char] = max(cb[char], b.count(char))

        res = []
        for a in A:

            if all(a.count(c) >= cb[c] for c in cb.keys()):
                res.append(a)

        return res
