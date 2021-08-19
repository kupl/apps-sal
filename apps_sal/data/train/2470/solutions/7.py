class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        res = 0
        for i in dominoes:
            i = sorted(i)
            if str(i) not in d:
                d[str(i)] = 0
            d[str(i)] += 1
            if d[str(i)] > 1:
                res += d[str(i)] - 1
        print(d)
        return res
