import numpy as np
import collections


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        col = collections.defaultdict(list)
        lastx = {}
        ans = float('inf')
        for (x, y) in points:
            col[x].append(y)
        for (x, col_item) in sorted(col.items()):
            col_item = sorted(col_item)
            for i in range(len(col_item)):
                y2 = col_item[i]
                for j in range(i):
                    y1 = col_item[j]
                    x1 = lastx.get((y1, y2))
                    if x1 != None:
                        ans = min(ans, (x - x1) * (y2 - y1))
                    lastx[y1, y2] = x
        if ans < float('inf'):
            return ans
        else:
            return 0
