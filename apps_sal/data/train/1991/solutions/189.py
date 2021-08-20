from collections import deque


class Solution:

    def rec(self, curr, finish, fuel_left, dp, locations, p):
        cnt = 0
        if curr == finish:
            cnt = 1
        n = len(locations)
        for i in range(n):
            if i != curr and fuel_left - abs(locations[i] - locations[curr]) >= 0:
                if dp[fuel_left - abs(locations[i] - locations[curr])][i] != -1:
                    cnt = (cnt + dp[fuel_left - abs(locations[i] - locations[curr])][i]) % p
                else:
                    cnt = (cnt + self.rec(i, finish, fuel_left - abs(locations[i] - locations[curr]), dp, locations, p)) % p
        dp[fuel_left][curr] = cnt % p
        return cnt % p

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        p = 1000000007
        dp = [[-1 for i in range(n)] for j in range(fuel + 1)]
        return self.rec(start, finish, fuel, dp, locations, p)
