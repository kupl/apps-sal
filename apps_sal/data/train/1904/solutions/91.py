import heapq


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        max_heap = []
        for i in range(len(points)):
            sqrt = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(max_heap, [sqrt, points[i]])
        res = []
        for i in range(K):
            temp = heapq.heappop(max_heap)
            res.append(temp[1])
        return res
