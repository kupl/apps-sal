from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        # build maxCountB
        maxCountB = {}
        for w in B:
            c = Counter(w)
            for k, cnt in list(c.items()):
                maxCountB[k] = max(maxCountB.get(k, 0), cnt)

        res = []
        for w in A:
            c = Counter(w)
            isUniversal = True
            for k, cnt in list(maxCountB.items()):
                if k not in c or cnt > c[k]:
                    isUniversal = False
                    break
            if isUniversal:
                res.append(w)

        return res
