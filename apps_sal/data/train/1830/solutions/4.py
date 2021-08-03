'''
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ret = []
        def dfs(i, has_water, ans):
            i#print(i, has_water,ans)
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
        # min heap to store the days when flooding would happen (if lake not dried)
        nearest = []
        # dict to store all rainy days
        # use case: to push the subsequent rainy days into the heap for wet lakes
        locs = collections.defaultdict(collections.deque)
        # result - assume all days are rainy
        res = [-1] * len(rains)

        # preprocessing - {K: lake, V: list of rainy days}
        for i, lake in enumerate(rains):
            locs[lake].append(i)

        for i, lake in enumerate(rains):
            # the nearest lake got flooded (termination case)
            if nearest and nearest[0] == i:
                return []

            # lake got wet
            if lake != 0:
                # pop the wet day
                locs[lake].popleft()

                # priotize the next rainy day for this lake
                if locs[lake]:
                    nxt = locs[lake][0]
                    heapq.heappush(nearest, nxt)
            # a dry day
            else:
                # no wet lake, append an arbitrary value
                if not nearest:
                    res[i] = 1
                else:
                    # dry the lake that has the highest priority
                    # since that lake will be flooded in nearest future otherwise (greedy property)
                    next_wet_day = heapq.heappop(nearest)
                    wet_lake = rains[next_wet_day]
                    res[i] = wet_lake

        return res
