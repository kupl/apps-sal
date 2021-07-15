from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = defaultdict(deque)
        
        for day, lake in enumerate(rains):
            lakes[lake].append(day)
        
        N = len(rains)
        need = SortedList()
        res = [1]*N
        
        for curr_day, lake in enumerate(rains):
            if lake:
                lakes[lake].popleft()
                
                if len(lakes[lake]) > 0:
                    next_lake_index = lakes[lake][0]
                    need.add(next_lake_index)
                
                res[curr_day] = -1
            elif need:
                chosen_lake_index = need.pop(0)
                if chosen_lake_index < curr_day:
                    return []
                
                res[curr_day] = rains[chosen_lake_index]
        
        return res if not need else []
                
                
                
        
                
                

