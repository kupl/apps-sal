class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        counter = Counter(list(map(tuple, points)))
        if any(count >= 4 for count in list(counter.values())):
            return 0
        points = list(counter)
        result = float('inf')
        for i, (x, y) in enumerate(points):
            for j in range(i + 1, len(points)):
                x_, y_ = points[j]
                if x != x_ and y != y_:
                    if (x, y_) in counter and (x_, y) in counter:
                        result = min(result, abs((x_ - x) * (y_ - y)))
                        if not result:
                            return 0
                elif counter[(x, y)] == 2 and counter[(x_, y_)] == 2:
                        return 0
        return 0 if result == float('inf') else result

