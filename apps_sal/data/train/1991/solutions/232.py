def solve(locations, curr, end, dp, fuel):
    if(fuel < 0):
        return 0
    if(dp[curr][fuel] != -1):
        return dp[curr][fuel]
    if(curr == end):
        ans = 1
    else:
        ans = 0
    for j in range(len(locations)):
        if(j != curr):
            ans = (ans + solve(locations, j, end, dp, fuel - abs(locations[j] - locations[curr]))) % 1000000007
    dp[curr][fuel] = ans
    return dp[curr][fuel]


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1 for i in range(fuel + 1)] for j in range(len(locations))]
        return solve(locations, start, finish, dp, fuel)
