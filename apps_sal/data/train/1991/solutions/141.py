class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        '''n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        ds = locations[start]
        de = locations[finish]
        locations.sort()'''
        mod = 10 ** 9 + 7
        n = len(locations)
        @lru_cache(None)
        def dfs(cur, remain):
            if abs(locations[finish] - locations[cur]) > remain:
                return 0
            res = 0
            if cur == finish:
                res = 1
            for i in range(n):
                if i == cur:
                    continue
                temp =  abs(locations[i] - locations[cur])
                if temp <= remain:
                    res = (res + dfs(i, remain - temp)) % mod
            return res
        return dfs(start, fuel)
