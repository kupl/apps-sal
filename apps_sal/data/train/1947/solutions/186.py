class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = collections.Counter()

        for w in B:
            for c, n in collections.Counter(w).items():
                d[c] = max(n, d[c])  # max(2,1)
        res = []
        for w in A:
            t = collections.Counter(w)
            if all(t[x] >= d[x] for x in d):
                res.append(w)
        return res
