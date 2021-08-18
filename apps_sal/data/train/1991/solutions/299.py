class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 1000000007
        n = len(locations)

        @functools.lru_cache(None)
        def dfs(cur, target, tot):
            res = 0
            for i in range(n):
                if i == cur:
                    if i == finish:
                        res += 1

                    continue
                if tot + abs(locations[cur] - locations[i]) > fuel:
                    continue
                else:
                    res += dfs(i, target, tot + abs(locations[cur] - locations[i]))
                    res %= mod
            return res
        return dfs(start, finish, 0)
