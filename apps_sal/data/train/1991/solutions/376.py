class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mem={}
        
        def count(start,end,fuel,mem):
            if fuel==0 and start!=end:
                return 0
            if not mem.get((start,fuel)) is None:
                return mem[(start,fuel)]
            res=0
            if start==end:
                res=1
            for i in range(len(locations)):
                if i!=start and abs(locations[i]-locations[start])<=fuel:
                    res+=count(i,end,fuel-abs(locations[i]-locations[start]),mem)
            mem[(start,fuel)]=res%(10**9+7)
            return mem[(start,fuel)]
        
        res=count(start,finish,fuel,mem)
        return res

