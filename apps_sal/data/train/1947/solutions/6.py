from collections import Counter


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        h = {}
        for word in B:
            temp = Counter(word)
            for (key, value) in temp.items():
                if key not in h:
                    h[key] = value
                else:
                    h[key] = max(h[key], value)
        res = []
        for word in A:
            temp = Counter(word)
            suitable = True
            for (key, value) in h.items():
                if not (key in temp and value <= temp[key]):
                    suitable = False
                    break
            if suitable:
                res.append(word)
        return res
