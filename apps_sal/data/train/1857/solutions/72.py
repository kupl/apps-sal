from collections import defaultdict


class Solution:

    def maxNumberOfFamilies(self, n: int, R: List[List[int]]) -> int:
        dic = defaultdict(set)
        for (x, y) in R:
            dic[x].add(y)
        res = 2 * (n - len(dic))
        for v in list(dic.values()):
            if all((j not in v for j in (2, 3, 4, 5))):
                res += 1 + all((j not in v for j in (6, 7, 8, 9)))
            else:
                res += (6 not in v and 7 not in v) and (4 not in v and 5 not in v or (8 not in v and 9 not in v))
        return res
