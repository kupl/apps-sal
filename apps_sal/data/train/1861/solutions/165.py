class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        counter = Counter(list(map(tuple, points)))
        points = list(counter)
        result = float('inf')
        for i, (x, y) in enumerate(points):
            for j in range(i + 1, len(points)):
                x_, y_ = points[j]
                if x != x_ and y != y_:
                    area = abs((x_ - x) * (y_ - y))
                    if area < result and (x, y_) in counter and (x_, y) in counter:
                        if not area:
                            return 0
                        result = area
                elif counter[(x, y)] == 2 and counter[(x_, y_)] == 2:
                        return 0
        return 0 if result == float('inf') else result

