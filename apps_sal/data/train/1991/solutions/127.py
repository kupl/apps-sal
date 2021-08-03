from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(pos, f):
            out = 0
            if pos == finish:
                out += 1
            for i, x in enumerate(locations):
                if i != pos and f >= abs(x - locations[pos]):
                    out += dfs(i, f - abs(x - locations[pos]))
                    out %= mod
            return out

        return dfs(start, fuel)
