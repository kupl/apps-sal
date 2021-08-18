class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        distance_map = list(map(lambda x: (x, x[0] ** 2 + x[1] ** 2), points))
        from queue import PriorityQueue
        heap = PriorityQueue(K)

        for points, dist in distance_map:
            if not heap.full():
                heap.put((-dist, points))
            elif dist < - heap.queue[0][0]:
                _ = heap.get()
                heap.put((-dist, points))

        res = []
        while not heap.empty():
            res.append(heap.get()[1])
        return res
