# Time Complexity: O(NlogK)
# Space Complexity: O(K)

from heapq import *

# Approach 1 - Succinct code
# class Solution:
#     def distance(self, point):
#         # ignoring sqrt to calculate the distance
#         return point[0] ** 2 + point[1] ** 2
#
#     def kClosest(self, points, K):
#         '''
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         '''
#         max_heap = []
#         for point in points:
#             heappush(max_heap, (-self.distance(point), point))
#             if len(max_heap) > K:
#                 heappop(max_heap)
#
#         res = []
#         while max_heap:
#             res.append(heappop(max_heap)[1])
#         return res


# Approach 2 - Define a Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        # for comparison we ignore the sqrt part
        return self.x ** 2 + self.y ** 2

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()


class Solution:
    def kClosest(self, points, K):
        '''
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        '''
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
