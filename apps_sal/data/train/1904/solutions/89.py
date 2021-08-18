import math
from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue()
        for point in points:
            dist = math.sqrt((0 - abs(point[0]))**2 + (0 - abs(point[1]))**2)
            pq.put((dist, tuple(point)))
        i = 0
        res = []
        while pq and i < K:
            res.append(pq.get()[1])
            i += 1
        return res
