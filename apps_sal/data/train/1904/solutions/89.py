import math
from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # dist_map = dict()
        # for point in points:
        #     dist_map[tuple(point)] = math.sqrt((0-abs(point[0]))**2 + (0-abs(point[1]))**2)
        # closest_points = sorted(dist_map.items(), key=lambda x: x[1])
        # return [i[0] for i in list(closest_points)[:K]]
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
