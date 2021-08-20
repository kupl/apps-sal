class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        fullLake = {}
        dry = {}
        for (day, lake) in enumerate(rains):
            if lake not in fullLake:
                if lake:
                    fullLake[lake] = day
            elif lake:
                dry[fullLake[lake]] = day
                fullLake[lake] = day
        heap = []
        for (day, lake) in enumerate(rains):
            if heap and day >= heap[0][0]:
                return []
            if lake:
                if day in dry:
                    heapq.heappush(heap, (dry[day], lake))
                rains[day] = -1
            elif heap:
                rains[day] = heapq.heappop(heap)[1]
            else:
                rains[day] = 1
        return rains
