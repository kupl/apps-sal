class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        u = {c: 0 for c in letters}
        for w in B:
            for (c, f) in list(Counter(w).items()):
                u[c] = max(u[c], f)
        res = []
        for w in A:
            wc = Counter(w)
            if all((f <= wc[c] for (c, f) in list(u.items()))):
                res.append(w)
        return res
