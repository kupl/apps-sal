class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set((r,c) for r,c in points)
        m = 2 ** 32
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i, len(points)):
                x2,y2 = points[j]
                if x2 == x1 or y2 == y1:
                    continue
                if (x2,y1) not in points_set:
                    continue
                if (x1,y2) not in points_set:
                    continue
                area = abs(x1-x2) * abs(y1 - y2)
                m = min(m,area)
        if m == 2**32:
            return 0
        else:
            return m
