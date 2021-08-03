class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mem = {}
        MOD = 10**9 + 7

        def dp(i, gas):
            if gas < 0:
                return 0
            if (i, gas) in mem:
                return mem[(i, gas)]

            res = 0
            if i == finish:
                res += 1

            for j in range(len(locations)):
                dist = abs(locations[j] - locations[i])
                if i == j or dist > gas:
                    continue
                res += dp(j, gas - dist)

            mem[(i, gas)] = res % MOD
            return res

        return dp(start, fuel) % MOD
