class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        DP = [[-1 for j in range(fuel + 1)] for j in range(n)]
        return self.helper(locations, start, finish, DP, fuel) % (10 ** 9 + 7)

    def helper(self, locations, curr, end, DP, fuel):
        if fuel < 0:
            return 0
        if DP[curr][fuel] != -1:
            return DP[curr][fuel]
        ans = 1 if curr == end else 0
        for next_ in range(len(locations)):
            if next_ != curr:
                ans += self.helper(locations, next_, end, DP, fuel - abs(locations[next_] - locations[curr]))
        DP[curr][fuel] = ans
        return ans
