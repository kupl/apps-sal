import math as m


class Solution(object):
    def dist(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return m.sqrt(dx * dx + dy * dy)

    def intersect(self, p1, p2, r):
        res = []
        d = self.dist(p1, p2) - 2 * r
        if (d > 0):
            res = []
        elif (d == 0):
            res = [[(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]]
        else:
            mid_x = (0.0 + p1[0] + p2[0]) / 2
            mid_y = (0.0 + p1[1] + p2[1]) / 2
            if (p1[1] != p2[1]):
                ratio = - (0.0 + p1[0] - p2[0]) / (0.0 + p1[1] - p2[1])
                eps = m.sqrt((r ** 2 - self.dist([mid_x, mid_y], p1) ** 2) / (ratio ** 2 + 1))
                fun = eps * ratio
            else:
                eps = 0
                fun = m.sqrt(r ** 2 - self.dist([mid_x, mid_y], p1) ** 2)
            res = [[mid_x + eps, mid_y + fun], [mid_x - eps, mid_y - fun]]
        return res

    def numPoints(self, points, r):
        l = len(points)
        result = 1
        for i in range(l):
            for j in range(i + 1, l):
                c = self.intersect(points[i], points[j], r)
                for p in c:
                    au = 0
                    for k in range(l):
                        if (self.dist(p, points[k]) <= r):
                            au += 1
                    result = max(result, au)
        return result
