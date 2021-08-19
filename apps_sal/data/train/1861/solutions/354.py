class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float('inf')
        seen = set(map(tuple, points))
        points.sort()
        for i in range(len(points)):
            for j in range(i):
                (x1, y1) = (points[i][0], points[i][1])
                (x2, y2) = (points[j][0], points[j][1])
                if x1 != x2 and y1 != y2 and ((x1, y2) in seen) and ((x2, y1) in seen):
                    ans = min(ans, (x1 - x2) * abs(y2 - y1))
        return ans if ans != float('inf') else 0
