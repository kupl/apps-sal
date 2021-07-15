class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:     
        cache={}
        def countPaths(start,fuel):
            if cache.get((start,fuel))!=None:
                return cache[(start,fuel)]
            # if fuel==0 and start==finish:
            #     return 1
            # if fuel==0 and start!=finish:
            #     return 0
            
            s=0
            if fuel<0:
                return 0
            if start==finish:
                s+=1
            for i in range(len(locations)):
                
                if i==start:
                    continue
                # if i==finish:
                #     s+=1
                s+=countPaths(i,fuel-abs(locations[start]-locations[i]))
                s%=(pow(10,9)+7)
            cache[(start,fuel)]=s%(pow(10,9)+7)
            return cache[(start,fuel)]
        # if start==finish:
        #     return 1+countPaths(start,fuel)
        return countPaths(start,fuel)
