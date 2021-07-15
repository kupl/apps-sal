class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7
        def dfs(cur_loc, fuel):
            if (cur_loc, fuel) in mem:
                return mem[(cur_loc, fuel)]
            if fuel < 0: return 0
            ans = 0
            if cur_loc == finish: ans = 1
            for i in range(len(locations)):
                if cur_loc == i: continue
                ans += dfs(i, fuel - abs(locations[cur_loc] - locations[i]))
            mem[(cur_loc, fuel)] = ans
            return ans
        mem = {}
        return dfs(start, fuel) % mod

