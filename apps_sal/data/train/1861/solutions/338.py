class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        d = set(map(tuple, points))

        min_square = sys.maxsize
        for i, x in enumerate(points):
            for j in range(i, len(points)):
                y = points[j]
                if x[0] != y[0] and x[1] != y[1] and (x[0], y[1]) in d and (y[0], x[1]) in d:
                    min_square = min(min_square, abs(x[0] - y[0]) * abs(x[1] - y[1]))

        return min_square if min_square != sys.maxsize else 0
