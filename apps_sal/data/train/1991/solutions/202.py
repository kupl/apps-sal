class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1 for i in range(len(locations))] for j in range(fuel + 1)]
        out = self.helper(locations, start, finish, fuel, dp, start)
        return out % 1000000007

    def helper(self, locations, start, finish, fuel, dp, index):
        if fuel < 0:
            return 0
        if dp[fuel][index] != -1:
            return dp[fuel][index]
        if index == finish:
            ans = 1
            for i in range(len(locations)):
                if i != index:
                    ans += self.helper(locations, start, finish, fuel - abs(locations[i] - locations[index]), dp, i)
        else:
            ans = 0
            for i in range(len(locations)):
                if i != index:
                    ans += self.helper(locations, start, finish, fuel - abs(locations[i] - locations[index]), dp, i)
        dp[fuel][index] = ans
        return ans
