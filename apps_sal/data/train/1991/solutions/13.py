class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dfs(i, f):
            res = 1 if i == e_idx else 0
            for j in range(i - 1, -1, -1):
                df = locations[i] - locations[j]
                if df > f:
                    break
                res += dfs(j, f - df)
            for j in range(i + 1, len(locations)):
                df = locations[j] - locations[i]
                if df > f:
                    break
                res += dfs(j, f - df)
            return res
        (s_loc, e_loc) = (locations[start], locations[finish])
        locations.sort()
        (s_idx, e_idx) = (locations.index(s_loc), locations.index(e_loc))
        return dfs(s_idx, fuel) % (10 ** 9 + 7)
