class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        closest = []
        locs = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        ret = []
        for i, lake in enumerate(rains):
            if closest and closest[0] == i:
                return []
            if not lake:
                if not closest:
                    ret.append(1)
                    continue
                nxt = heapq.heappop(closest)
                ret.append(rains[nxt])
            else:
                l = locs[lake]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
                ret.append(-1)
        return ret
