class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = defaultdict(deque)
        
        for day, lake in enumerate(rains):
            lakes[lake].append(day)
        
        N = len(rains)
        res = [1]*N
        heap = [] # days in order of indicies
        
        for day, lake in enumerate(rains):
            if lake:
                lakes[lake].popleft() # current
                if lakes[lake]:
                    next_lake_day = lakes[lake][0]
                    heappush(heap, next_lake_day)
                res[day] = -1
            else:
                if heap:
                    chosen_day = heappop(heap)
                    if chosen_day < day:
                        return []
                    res[day] = rains[chosen_day]
        
        return res if not heap else []
                
                

