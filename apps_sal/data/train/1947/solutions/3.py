from collections import Counter as di


class Solution:

    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        d = di()
        ans = list()
        for i in b:
            d2 = di(i)
            for (k, v) in d2.items():
                if d[k] < d2[k]:
                    d[k] = v
        for i in a:
            if len(d - di(i)) == 0:
                ans.append(i)
        return ans
