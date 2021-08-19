class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        ans = float('inf')
        s = set(map(tuple, points))
        for (i, p2) in enumerate(points):
            for j in range(i):
                p1 = points[j]
                if p2[0] != p1[0] and p2[1] != p1[1] and ((p1[0], p2[1]) in s) and ((p2[0], p1[1]) in s):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0
