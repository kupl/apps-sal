class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        '''
        f(s, cost) 
        '''
        def cost(i, j): return abs(locations[i] - locations[j])
        n, MOD = len(locations), 10**9 + 7

        @functools.lru_cache(None)
        def solve(s, fuel):
            if fuel < 0:
                return 0
            ans = 1 if s == finish else 0
            for t in range(n):
                if s == t:
                    continue
                ans += solve(t, fuel - cost(s, t))
            return ans % MOD

        return solve(start, fuel)
