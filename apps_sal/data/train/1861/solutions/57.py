import collections


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        dic = collections.defaultdict(list)
        for (x, y) in points:
            dic[x].append(y)
        res = float('inf')
        store = {}
        for x in sorted(dic):
            col = sorted(dic[x])
            for (i, y1) in enumerate(col):
                for j in range(i):
                    if (y1, col[j]) not in store:
                        store[y1, col[j]] = x
                    else:
                        res = min(res, (y1 - col[j]) * (x - store[y1, col[j]]))
                        store[y1, col[j]] = x
        return res if res != float('inf') else 0
