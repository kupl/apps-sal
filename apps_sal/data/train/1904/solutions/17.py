from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue()

        for p in points:  # O(nlogk)
            new_priority = -1 * (p[0] * p[0] + p[1] * p[1])
            if pq.qsize() == K:
                old_priority, old_point = pq.get()
                if new_priority > old_priority:
                    pq.put((new_priority, p))
                else:
                    pq.put((old_priority, old_point))
            else:
                pq.put((new_priority, p))

        res = []
        for i in range(K):
            priority, p = pq.get()
            res.append(p)

        return res
