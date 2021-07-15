class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)
        
        @functools.lru_cache(None)
        def recur(curr, rest):
            res = 1 if curr == finish else 0
            for i in range(n):
                cost = abs(locations[curr] - locations[i])
                if curr != i and cost <= rest:
                    res += recur(i, rest - cost)
            return res
        
        return recur(start, fuel) % MOD

