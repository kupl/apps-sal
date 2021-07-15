from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def DP(cur, fuel):
            if fuel < 0:
                return 0
            return (int(cur == finish) + sum(
                DP(nxt, fuel - abs(locations[cur] - locations[nxt]))
                for nxt in range(len(locations))
                if nxt != cur
            )) % MOD

        return DP(start, fuel)

