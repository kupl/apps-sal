class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(None)
        def solve(s, e, f):
            res = 0 if s != e else 1
            for i, v in enumerate(locations):
                if i == s:
                    continue
                cost = abs(locations[s] - locations[i])
                if cost > f:
                    continue
                res += solve(i, e, f - cost)
            return res
        return solve(start, finish, fuel) % int(1e9 + 7)
