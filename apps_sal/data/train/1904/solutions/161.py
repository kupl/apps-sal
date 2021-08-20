from queue import PriorityQueue


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue()
        for (i, c) in enumerate(points):
            pq.put((c[0] * c[0] + c[1] * c[1], i))
        res = []
        for j in range(K):
            pair = pq.get()
            res.append(points[pair[1]])
        return res
