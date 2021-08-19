class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def dp(curr_loc, fuel):
            if (curr_loc, fuel) in memo:
                return memo[curr_loc, fuel]
            if fuel < 0:
                return 0
            ans = 0
            if curr_loc == finish:
                ans = 1
            for (i, loc) in enumerate(locations):
                if i != curr_loc:
                    ans += dp(i, fuel - abs(locations[curr_loc] - loc))
            memo[curr_loc, fuel] = ans
            return ans
        memo = {}
        return dp(start, fuel) % (10 ** 9 + 7)
