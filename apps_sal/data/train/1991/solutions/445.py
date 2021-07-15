class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        dp = [[0 for x in range(len(locations))] for _ in range(fuel+1)]

        #At the begining there is one way of getting to start point without using any fuel
        dp[0][start] = 1

        for i in range(1,fuel+1):
           for j in range(len(locations)):
           #k is origin from where I go to location j
            for k in range(len(locations)):
                if j!=k:
                    need = abs(locations[j]-locations[k])
                    if need <= i:
                        dp[i][j] += dp[i-need][k]

        ans = 0
        #Sum up over all paths leading to finish, for every possible amount of fuel
        for i in range(fuel+1):
           ans += dp[i][finish]

        return ans % mod
