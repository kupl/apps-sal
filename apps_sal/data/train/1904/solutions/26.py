import queue
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # priority queue (minheap)
        # put distance: index of points
        if not points: return []
        q = queue.PriorityQueue()
        for l in points:
            # put negative distance to make heap as max heap
            q.put((-(l[0]**2 + l[1]**2), l))
            if q.qsize() > K:
                q.get()
        res = []
        while K > 0:
            res.append(q.get()[1])
            K -= 1
        return res
            

