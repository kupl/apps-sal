import math
import heapq


class Solution:

    def getEuclideanDistance(self, p1):
        return math.sqrt(p1[0] ** 2 + p1[1] ** 2)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        kheap = []
        heapq.heapify(kheap)
        size = 0
        for (i, point) in enumerate(points):
            heapq.heappush(kheap, (-self.getEuclideanDistance(point), i))
            size += 1
            if size > K:
                heapq.heappop(kheap)
        kpoints = []
        while kheap:
            (dist, ind) = heapq.heappop(kheap)
            kpoints.append(points[ind])
        return kpoints
