from queue import PriorityQueue


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue()
        for p in points:
            distance = -1 * (p[0] * p[0] + p[1] * p[1])
            if pq.qsize() < K:
                pq.put((distance, p))
            else:
                pq.put((distance, p))
                pq.get()
        ans = []
        while pq.qsize():
            (distance, p) = pq.get()
            ans.append(p)
        return ans
