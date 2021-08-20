class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        from collections import defaultdict, deque
        closest = []
        locs = defaultdict(deque)
        res = []
        for (i, lake) in enumerate(rains):
            locs[lake].append(i)
        for (i, rain) in enumerate(rains):
            if closest and closest[0] == i:
                return []
            if rain:
                locs[rain].popleft()
                if locs[rain]:
                    heapq.heappush(closest, locs[rain][0])
                res.append(-1)
            elif closest:
                dry = heapq.heappop(closest)
                res.append(rains[dry])
            else:
                res.append(1)
        return res
