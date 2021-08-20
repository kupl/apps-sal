class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        if len(B) == 0:
            return A
        from collections import Counter
        cb = Counter(B[0])
        for i in range(1, len(B)):
            c = Counter(B[i])
            for ch in c.keys():
                cb[ch] = max(cb[ch], c[ch])
        res = []
        for a in A:
            add = True
            ca = Counter(a)
            for keyB in cb.keys():
                if keyB not in ca or cb[keyB] > ca[keyB]:
                    add = False
            if add:
                res.append(a)
        return res
