class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pts = set()
        for p in points:
            pts.add((p[0], p[1]))
        ans = float('inf')
        flag = False
        P = len(points)
        for i in range(P):
            for j in range(i + 1, P):
                if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                    continue
                else:
                    dx1 = points[i][0]
                    dy1 = points[j][1]
                    dx2 = points[j][0]
                    dy2 = points[i][1]
                    if (dx1, dy1) in pts and (dx2, dy2) in pts:
                        area = abs(dy1 - dy2) * abs(dx1 - dx2)
                        ans = min(area, ans)
                        flag = True
        return ans if flag else 0
