class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # get_distance = lambda x: x[0] **2 + x[1] **2
        # tmp = list(map(lambda x: [x[0], x[1], get_distance(x)], points))
        # # print(tmp)
        # tmp.sort(key=lambda x: x[2])
        # res = list(map(lambda x: [x[0], x[1]], tmp[:K]))
        # return res
        
        distance_map = list(map(lambda x: (x, x[0] **2 + x[1] **2), points))
        from queue import PriorityQueue
        heap = PriorityQueue(K)
        
        for points, dist in distance_map:
            if not heap.full():
                heap.put((-dist, points))
                # print(heap.queue)
                # print(heap.queue[0][0])
            elif dist < - heap.queue[0][0]:
                # print('heap', heap.queue)
                _ = heap.get()
                heap.put((-dist, points))
            
        res = []
        while not heap.empty():
            res.append(heap.get()[1])
        return res
