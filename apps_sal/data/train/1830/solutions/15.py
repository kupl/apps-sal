class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        lake_to_days = collections.defaultdict(list)
        full_lakes = set()
        to_empty = []
        
        for day, lake in enumerate(rains):
            lake_to_days[lake].append(day)
        
        for day in range(len(rains)):
            lake = rains[day]
            if lake:
                if lake in full_lakes:
                    return []
                full_lakes.add(lake)
                lake_to_days[lake].pop(0)
                if lake_to_days[lake]:
                    heapq.heappush(to_empty, lake_to_days[lake][0])
            else:
                if to_empty:
                    ans[day] = rains[heapq.heappop(to_empty)]
                    full_lakes.remove(ans[day])
                else:
                    ans[day] = 1
        return ans
        
        
                    
        
        
        
            

