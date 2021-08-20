from heapq import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = x ** 2 + y ** 2

    def __lt__(self, other):
        return self.distance > other.distance


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_heap = []
        for (x, y) in points:
            if len(distance_heap) >= K:
                if Point(x, y) > distance_heap[0]:
                    heappop(distance_heap)
                    heappush(distance_heap, Point(x, y))
            else:
                heappush(distance_heap, Point(x, y))
        res = []
        while distance_heap:
            point = heappop(distance_heap)
            res.append([point.x, point.y])
        return res
