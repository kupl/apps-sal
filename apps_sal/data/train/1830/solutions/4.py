'''
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ret = []
        def dfs(i, has_water, ans):
            i
            nonlocal ret
            if ret: return
            if i == n:  ret = ans; return 
            if rains[i] in has_water:  return 
            if rains[i]:  dfs(i+1, has_water|set([rains[i]]), ans+[-1])
            else:
                if not has_water: dfs(i+1, has_water, ans+[1])
                for lake in has_water:
                    has_water.remove(lake)
                    dfs(i+1, has_water, ans+[lake])
                    has_water.add(lake)
        dfs(0, set(), [])
        return ret
                    
'''


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        nearest = []
        locs = collections.defaultdict(collections.deque)
        res = [-1] * len(rains)

        for i, lake in enumerate(rains):
            locs[lake].append(i)

        for i, lake in enumerate(rains):
            if nearest and nearest[0] == i:
                return []

            if lake != 0:
                locs[lake].popleft()

                if locs[lake]:
                    nxt = locs[lake][0]
                    heapq.heappush(nearest, nxt)
            else:
                if not nearest:
                    res[i] = 1
                else:
                    next_wet_day = heapq.heappop(nearest)
                    wet_lake = rains[next_wet_day]
                    res[i] = wet_lake

        return res
