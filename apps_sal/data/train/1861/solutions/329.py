from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        ss = set([tuple(ele) for ele in points])
        ans = float('inf')

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if (x2, y1) in ss and (x1, y2) in ss and x1 != x2 and y1 != y2:
                    ans = min(ans, abs((x1 - x2) * (y1 - y2)))
        return (0 if ans == float('inf') else ans)
