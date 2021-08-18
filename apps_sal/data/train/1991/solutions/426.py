class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = []
        for i in range(len(locations)):
            dp.append([-1] * (fuel + 1))

        def count(dest: int, fuel_left: int) -> int:
            if fuel_left > fuel:
                return 0
            if dp[dest][fuel_left] != -1:
                return dp[dest][fuel_left]
            if fuel_left == fuel:
                if dest == start:
                    dp[dest][fuel] = 1
                    return 1
                dp[dest][fuel] = 0
                return 0
            ret = 0
            for i in range(len(locations)):
                if i == dest:
                    continue
                consume = abs(locations[dest] - locations[i])
                ret += count(i, fuel_left + consume)
            dp[dest][fuel_left] = ret
            return ret

        ret = 0
        for i in range(fuel + 1):
            partial = count(finish, i)
            ret += partial
        return ret % (10**9 + 7)
