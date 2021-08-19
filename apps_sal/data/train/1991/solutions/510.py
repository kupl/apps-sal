class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dfs(i, f):
            if not f:
                return int(i == finish)
            s = 0
            for j in range(len(locations)):
                cost = abs(locations[i] - locations[j])
                if i != j and f >= cost:
                    s += dfs(j, f - cost)
            return (s + int(i == finish)) % 1000000007
        return dfs(start, fuel)
