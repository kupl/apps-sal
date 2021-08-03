class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        memo = {}

        def solve(pos, fuel):
            if fuel == 0:
                return pos == finish
            elif (pos, fuel) in memo:
                return memo[(pos, fuel)]

            ret = pos == finish
            for i in range(len(locations)):
                if i != pos:
                    cost = abs(locations[i] - locations[pos])
                    if cost <= fuel:
                        ret += solve(i, fuel - cost) % mod

            memo[(pos, fuel)] = ret % mod
            return ret % mod

        return solve(start, fuel)
