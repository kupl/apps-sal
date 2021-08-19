class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # group points by x coord, for each pari of points in column,
        # check for the smallest rectangle with this pair of points as the right edge
        # Time Coplexity: O(N^2) N is the number of points
        # columns = collections.defaultdict(list)
        # for x, y in points:
        #     columns[x].append(y)
        # last_x = {}
        # res = float('inf')
        # for x in sorted(columns):
        #     column = columns[x]
        #     column.sort()
        #     for j, y2 in enumerate(column):
        #         for i in range(j):
        #             y1 = column[i]
        #             if (y1, y2) in last_x:
        #                 res = min(res, (y2 - y1) * (x - last_x[(y1, y2)]))
        #             last_x[(y1, y2)] = x
        # return res if res < float('inf') else 0

        # assume each pair of points form the diagnal of the rectangle, check if other points
        # exist in the set, if so, we have a candidate
        # Time Coplexity: O(N^2)
        s = set([(x, y) for x, y in points])
        res = float('inf')
        for i, point1 in enumerate(points):
            for j in range(i):
                point2 = points[j]
                x1, y1 = point1
                x2, y2 = point2
                # two point can't form diagnal if they are on the same line
                if x1 != x2 and y1 != y2 and (x1, y2) in s and (x2, y1) in s:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
        return res if res < float('inf') else 0
