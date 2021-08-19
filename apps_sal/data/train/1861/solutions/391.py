class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(((p[0], p[1]) for p in points))
        ans = float('inf')
        for i in range(len(points)):
            for j in range(i):
                p1 = points[i]
                p2 = points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                if (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0
