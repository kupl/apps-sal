from collections import defaultdict
from heapq import heapify, heappush, heappop


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        temp = []
        for i in points:
            dist = i[0] ** 2 + i[1] ** 2
            temp.append([dist, [i[0], i[1]]])
        heapify(temp)
        res = []
        for i in range(K):
            res.append(heappop(temp)[1])
        return res
