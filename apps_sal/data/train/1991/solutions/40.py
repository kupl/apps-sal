class Solution:
    def countRoutes(self, a: List[int], s: int, e: int, f: int) -> int:
        n = len(a)
        @lru_cache(None)
        def dfs(i, f):
            if f < 0: return 0            
            ans = int(i == e)
            for j in range(n):
                if j == i: continue
                dist = abs(a[i] - a[j])
                ans += dfs(j, f-dist)
            return ans
        return dfs(s, f) % (10**9+7)
