import queue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        q = queue.PriorityQueue()
        for l in points:
            q.put((-(l[0]**2 + l[1]**2), l))
            if q.qsize() > K:
                q.get()
        res = []
        while K > 0:
            res.append(q.get()[1])
            K -= 1
        return res
