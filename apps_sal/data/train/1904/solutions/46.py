from heapq import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return self.x ** 2 + self.y ** 2

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()


class Solution:

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        max_heap = []
        for p in points:
            point = Point(p[0], p[1])
            dist = point.distance_from_origin()
            heappush(max_heap, (-dist, point))
            if len(max_heap) > K:
                heappop(max_heap)
        res = []
        while max_heap:
            pt = heappop(max_heap)[1]
            res.append([pt.x, pt.y])
        return res
