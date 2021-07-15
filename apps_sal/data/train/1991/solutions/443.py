class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0] * len(locations) for _ in range(fuel+1)]
        dp[0][finish] = 1
        res = 0
        for curr_fuel in range(0, fuel+1):
            for pos, val in enumerate(locations):
                for pos2, val2 in enumerate(locations):
                    if pos2 != pos:
                        last_fuel = curr_fuel - abs(val - val2)
                        if last_fuel >= 0:
                            dp[curr_fuel][pos] += dp[last_fuel][pos2]
        
                if pos == start:
                    res = (res + dp[curr_fuel][pos]) % 1000000007
        return res
