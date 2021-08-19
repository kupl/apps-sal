class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points = [Point(x, y) for [x, y] in points]
        dic_x = collections.defaultdict(set)
        dic_y = collections.defaultdict(set)
        for p in points:
            dic_x[p.x].add(p.y)
            dic_y[p.y].add(p.x)
        area = math.inf
        for (p1, p2) in itertools.combinations(points, 2):
            if p1.x == p2.x or p1.y == p2.y:
                continue
            if p2.y in dic_x[p1.x] and p2.x in dic_y[p1.y]:
                area = min(area, abs(p2.x - p1.x) * abs(p2.y - p1.y))
        return area if area != math.inf else 0
