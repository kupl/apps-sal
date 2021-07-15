class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        d = defaultdict(lambda: defaultdict(int))

        
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, fuel):
            if fuel < 0:
                return 0
            if (i,fuel) in d:
                return d[i][fuel]
            else:
                if i == finish:
                    res = 1
                else:
                    res = 0
                for j in range(len(locations)):
                    expected = fuel- abs(locations[i] - locations[j])
                    if i != j and expected >= 0:
                        res+=dfs(j, expected)
                d[i][fuel] = res
                return res
        return dfs(start, fuel) % (10**9 + 7)
        #print(d[1])

