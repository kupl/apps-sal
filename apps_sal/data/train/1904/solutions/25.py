from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        kPq = PriorityQueue()
        cnt = 0
        for point in points:
            w = point[0] * point[0] + point[1] * point[1]
            kPq.put([-w, point])
            cnt += 1
            if cnt > K:
                kPq.get()
        r = []
        while not kPq.empty():
            item = kPq.get()
            r.append(item[1])
        return r


