from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        A = [(Counter(a), a) for a in A]
        B = [Counter(b) for b in B]

        req = {}
        for cntr in B:
            for k, v in list(cntr.items()):
                req[k] = max(req.get(k, 0), v)

        sol = [a for cntr, a in A if all(cntr.get(k, 0) >= v for k, v in list(req.items()))]
        return sol
