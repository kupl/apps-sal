class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def routes(start, fuel):
            if fuel<0:
                return 0
            answer=0
            #print('start:'+str(start)+', fuel:'+str(fuel)+', answer: '+str(answer))
            if start==finish:
                answer+=1
            for i in range(len(locations)):
                if i==start:
                    continue
                answer+=routes(i, fuel-abs(locations[i]-locations[start]))
            #print('start:'+str(start)+', fuel:'+str(fuel)+', answer: '+str(answer))
            return answer
        return routes(start, fuel)%1000000007
