from queue import PriorityQueue


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) == 0:
            return True

        pq = PriorityQueue()
        total_pnum = 0

        for trip in trips:
            pq.put((trip[1], trip[0]))
            pq.put((trip[2], -trip[0]))

        while pq.qsize() > 0:
            cur_loc, pnum = pq.get()
            total_pnum += pnum

            if total_pnum > capacity:
                return False

        return True
