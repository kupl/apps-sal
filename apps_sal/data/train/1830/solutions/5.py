class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        closest = []
        locations = collections.defaultdict(collections.deque)
        for index, lake in enumerate(rains):
            locations[lake].append(index)
        res = []
        for index, lake in enumerate(rains):
            if closest and closest[0] == index:
                return []
            if not lake:
                if not closest:
                    res.append(1) 
                    continue
                nxt = heapq.heappop(closest)
                res.append(rains[nxt])
            else:
                l = locations[lake]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
                res.append(-1)
        return res
