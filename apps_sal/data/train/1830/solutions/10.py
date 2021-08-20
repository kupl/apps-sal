class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        (floods, n, visited, water_heap) = (None, len(rains), defaultdict(int), [])
        for i in range(n - 1, -1, -1):
            if rains[i]:
                if rains[i] in visited:
                    floods = (i, visited[rains[i]], floods)
                visited[rains[i]] = i
        for i in range(n):
            if not rains[i]:
                while floods and floods[0] < i:
                    (start, end, floods) = floods
                    heapq.heappush(water_heap, (end, start))
                if not water_heap:
                    rains[i] = 1
                else:
                    (end, start) = heappop(water_heap)
                    if end < i:
                        return []
                    rains[i] = rains[end]
            else:
                rains[i] = -1
        if water_heap or floods:
            return []
        return rains
