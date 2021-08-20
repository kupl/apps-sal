class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(src, tar):
            if src == finish:
                if tar == 0:
                    return 1
            res = 1 if src == finish else 0
            for i in range(n):
                if i != src:
                    diff = abs(locations[i] - locations[src])
                    if tar >= diff:
                        res += dfs(i, tar - diff)
            return res
        return dfs(start, fuel) % mod
