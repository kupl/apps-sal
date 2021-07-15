class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        m = 10 ** 9 + 7
        n = len(locations)
        dp = [[-1 for _ in range(fuel+1)] for _ in range(n)]
        return self.helper(locations, start, finish, dp, fuel)
        
    def helper(self, locations, curr, end, dp, fuel):
        if fuel < 0:
            return 0
        if dp[curr][fuel] != -1:
            return dp[curr][fuel]
        if curr == end:
            res = 1
        else:
            res = 0

        for nxt in range(len(locations)):
            if nxt != curr:
                res += self.helper(locations, nxt, end, dp, fuel-abs(locations[curr]-locations[nxt]))
        dp[curr][fuel] = res % (10 ** 9 + 7)
        return dp[curr][fuel]
