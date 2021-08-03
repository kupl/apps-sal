# time complexity: O(26*(A+B))
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 1st step, construct the minimal word which is a superset of all words in B
        letters = 'abcdefghijklmnopqrstuvwxyz'
        u = {c: 0 for c in letters}
        for w in B:
            for c, f in list(Counter(w).items()):  # char, frequency
                u[c] = max(u[c], f)

        # 2nd step, find every word a in A such that u is a subset of a
        res = []
        for w in A:
            wc = Counter(w)
            if all(f <= wc[c] for c, f in list(u.items())):
                res.append(w)
        return res
