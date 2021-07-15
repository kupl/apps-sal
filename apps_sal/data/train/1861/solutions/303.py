class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        S = set(map(tuple, points))
        ans = float('inf')
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                        (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0

