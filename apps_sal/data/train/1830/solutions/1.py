class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        filled = {}
        deadline = {}
        for (day, lake) in enumerate(rains):
            if lake not in filled:
                if lake:
                    filled[lake] = day
            elif lake:
                deadline[filled[lake]] = day
                filled[lake] = day
        heap = []
        for (day, lake) in enumerate(rains):
            if heap and day >= heap[0][0]:
                return []
            if lake:
                if day in deadline:
                    heapq.heappush(heap, (deadline[day], lake))
                rains[day] = -1
            elif heap:
                rains[day] = heapq.heappop(heap)[1]
            else:
                rains[day] = 1
        return rains
