class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        n,m=len(locations),fuel+1
        MOD=10**9+7
#         @lru_cache(None)
#         def run(current, fuel):
#             ans=0
#             if current==finish:
#                 ans+=1
#             for i in range(n):
#                 if i==current:
#                     continue
#                 cost = abs(locations[i]-locations[current])
#                 if cost <= fuel:
#                     ans+=run(i, fuel-cost)
#             return ans%MOD
        
#         return run(start,fuel)%MOD
        dp = [[0]*n for _ in range(m)]
        
        for fuell in range(m):
            for current in range(n):
                ans=0
                if current==finish:
                    ans+=1
                for j in range(n):
                    if j==current:
                        continue
                    cost = abs(locations[j]-locations[current])
                    if cost <= fuell:
                        ans+=dp[fuell-cost][j]
                dp[fuell][current] = ans%MOD
        # print(dp)
        return dp[fuel][start]
