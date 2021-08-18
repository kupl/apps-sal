import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        if len(points) == 0:
            return []
        if K >= len(points):
            return points

        def euclidean(point):
            x, y = point
            return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        mod_points = []
        for point in points:
            dist = euclidean(point)
            mod_points.append((dist, point[0], point[1]))

        heapq.heapify(mod_points)

        ret_values = heapq.nsmallest(K, mod_points)
        ret_values = [[x, y] for dist, x, y in ret_values]

        return ret_values
