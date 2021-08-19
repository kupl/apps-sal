class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def solve(i, f):
            ans = 1 if i == finish else 0
            for (j, npos) in enumerate(locations):
                cost = abs(npos - locations[i])
                if i != j and cost <= f:
                    ans = (ans + solve(j, f - cost)) % MOD
            return ans
        return solve(start, fuel)
