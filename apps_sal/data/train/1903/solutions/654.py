class dsu:
    def __init__(self, n):
        self.ranks = [0] * n
        self.ids = list(range(n))
        pass

    def find(self, x):
        if x != self.ids[x]:
            self.ids[x] = self.find(self.ids[x])
            pass
        return self.ids[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        elif self.ranks[rx] == self.ranks[ry]:
            self.ids[ry] = rx
            self.ranks[rx] += 1
            pass
        elif self.ranks[rx] < self.ranks[ry]:
            self.ids[rx] = ry
            pass
        else:
            self.ids[ry] = rx
            pass
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = dsu(len(points))
        lst = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                t = (dist, i, j)
                lst.append(t)
                pass
            pass
        lst.sort()
        cost = 0
        for i in range(len(lst)):
            success = d.union(lst[i][1], lst[i][2])
            if success:
                cost += lst[i][0]
                pass
            pass
        return cost
