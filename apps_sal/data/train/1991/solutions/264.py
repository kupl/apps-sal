class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        # DP = [[-1 for _ in range(fuel+1)] for _ in range(N)]

        # for idx, x in enumerate(locations):
        #     dist = abs(x - locations[finish])
        #     print (idx, x, dist)
        #     if dist <= fuel:
        #         for y in range(dist, fuel+1):
        #             DP[idx][y] = 1
#         for x in locations:
#             dist = abs(x - locations[finish])
#             if dist <= fuel:
#                 for y in range(dist, fuel+1):
#                     DP[finish][y] = 1
                    
#         table = {}
#         for idx, x in enumerate(locations):
#             for idxy, y in enumerate(locations):
#                 table[(idx, idxy)] = abs(locations[idx] - locations[idxy])
                
#         for c in range(fuel+1):
#             for r in range(N):
#                 # if True or DP[r][c] > 0:
#                 for x in range(N):
#                     if x == r: continue
#                     dist = abs(table[(r, x)])
#                     if dist <= c:
#                         # print (r, c, \"going to\", x, \"cost\", dist, \"before\", DP[r][c], \" adding\", DP[x][c-dist])
#                         DP[r][c] += DP[x][c-dist]
#                         # print (\"after\", DP[r][c])
#                 DP[r][c] %= 1000000007
#                     # for y in range(c, N)
       # return DP[start][fuel] % 1000000007 
            
        # print (DP)
        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return 0
            # if DP[i][k] >= 0:
            #     return DP[i][k]
            ans = 1 if i == finish else 0
            for j in range(N):
                if i == j: continue
                ans += dp(j, k - abs(locations[i]-locations[j]))
            ans %= 1000000007
            # DP[i][k] = ans
            return ans
        return dp(start, fuel)
        

