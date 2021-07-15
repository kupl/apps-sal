class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ctr = collections.Counter()
        for word in B:
            ctr2 = collections.Counter(word)
            # ctr.setdefault()
            for key, val in ctr2.items():
                ctr[key] = max(val, ctr[key])
        ctr3 = collections.Counter()
        # for key, val in collections.Counter(
        res = []
        for w in A:
            ctr3 = collections.Counter(w)
            newCtr = collections.Counter()
            for key, val in ctr3.items():
                if key in ctr:
                    newCtr[key] = min(val, ctr[key])
            if newCtr == ctr:
                res.append(w)
        return res
