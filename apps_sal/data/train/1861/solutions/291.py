class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        from collections import defaultdict

        x_set, y_set = set(), set()
        for x, y in points:
            x_set.add(x)
            y_set.add(y)

        if len(x_set) == len(points) or len(y_set) == len(points):
            return 0

        # using a hash map to record {x:[y]}
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)

        visited = {}
        res = float('inf')

        # sort hash map, for every 2 ys in the current column, calculate area
        for col in sorted(columns):
            num_y = columns[col]
            num_y.sort()

            for i in range(len(num_y)):
                for j in range(i):
                    y1 = num_y[i]
                    y2 = num_y[j]

                    if (y1, y2) in visited:
                        col_prev = visited[(y1, y2)]
                        area = (y1 - y2) * (col - col_prev)
                        res = min(res, area)

                    visited[(y1, y2)] = col

        return res if res != float('inf') else 0
