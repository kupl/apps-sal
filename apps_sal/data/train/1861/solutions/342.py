class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float('inf')
        s = {tuple(point) for point in points}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                (p1, p2) = (points[i], points[j])
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                if (p1[0], p2[1]) in s and (p2[0], p1[1]) in s:
                    ans = min(ans, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        return ans if ans != float('inf') else 0
