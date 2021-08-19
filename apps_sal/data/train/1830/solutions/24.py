class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        nearest = []
        locs = defaultdict(deque)
        for (i, lake) in enumerate(rains):
            locs[lake].append(i)
        for (i, lake) in enumerate(rains):
            if nearest and nearest[0] == i:
                return []
            if lake == 0:
                if not nearest:
                    ans[i] = 1
                else:
                    n = heappop(nearest)
                    ans[i] = rains[n]
            else:
                locs[lake].popleft()
                if locs[lake]:
                    heappush(nearest, locs[lake][0])
        return ans
