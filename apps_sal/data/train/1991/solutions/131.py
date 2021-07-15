class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def fn(n, x): 
            \"\"\"Return all possible routes from n to finish with x fuel.\"\"\"
            if x < 0: return 0 # not going anywhere without fuel 
            ans = 0
            if n == finish: ans += 1
            for nn in range(len(locations)): 
                if nn != n: ans += fn(nn, x-abs(locations[n] - locations[nn]))
            return ans 
        
        return fn(start, fuel) % 1_000_000_007

# class Solution:
#     def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
#         self.sol = [[-1]*(fuel+1)]*len(locations)
#         self.dfs(start, fuel, locations, finish, 0)
#         print(self.sol)
    
#     def dfs(self, current, fuel, locations, end, local_ans):
#         print(self.sol)
#         if fuel<0:
#             return 0
#         if self.sol[current][fuel]==-1:
#             ans = 1 if current==end else 0
#             for index, i in enumerate(locations):
#                 if index==current:
#                     continue
#                 cost = abs(locations[current]-i)
#                 a = self.dfs(index, fuel-cost, locations, end, local_ans)
#                 ans = ans + a
#             print(ans)
#             self.sol[current][fuel] = ans
#         return self.sol[current][fuel]


    
    
# private long solve(int[] locations, int curCity, int e, long[][] dp, int fuel) {
#         // 4. There is no further way left.
#         if (fuel < 0) return 0;
#         if (dp[curCity][fuel] != -1) return dp[curCity][fuel];
#         // 3. Now, if we have atleast 1 way of reaching `end`, add 1 to the answer. But don't stop right here, keep going, there might be more ways :)
#         long ans = (curCity == e) ? 1 : 0;
#         for (int nextCity = 0; nextCity < locations.length; ++nextCity) {
#             // 1. Visit all cities except `curCity`.
#             if (nextCity != curCity) {
#                 // 2. Continue this process recursively.
#                 ans = (ans + solve(locations, nextCity, e, dp, fuel - Math.abs(locations[curCity] - locations[nextCity]))) % 1000000007;
#             }
#         }
#         return dp[curCity][fuel] = ans;
#     }
