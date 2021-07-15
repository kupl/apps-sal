class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod=pow(10,9)+7
        @lru_cache(None)
        def dp(now,fuel):
            # print(now,fuel,abs(locations[now]-locations[finish]))
            if fuel<abs(locations[now]-locations[finish]):
                return 0
            res=1 if now!=finish else 0
            for nxt in range(len(locations)):
                if nxt!=now:
                    dis1=abs(locations[nxt]-locations[now])
                    dis2=abs(locations[nxt]-locations[finish])
                    # print(nxt,dis1,dis2)
                    if dis1+dis2<=fuel:
                        res+=dp(nxt,fuel-dis1)
                    # print('a',now,nxt,dis1,dis2,res)
            
            return res%mod
        return dp(start,fuel)%mod if start!=finish else (dp(start,fuel)+1)%mod
