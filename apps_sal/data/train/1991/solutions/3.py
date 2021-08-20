class Solution:

    def countRoutes(self, a: List[int], s: int, e: int, f: int) -> int:

        @lru_cache(None)
        def dfs(i, f):
            if f < 0:
                return 0
            ans = int(i == e)
            for j in range(len(a)):
                if j != i:
                    ans += dfs(j, f - abs(a[i] - a[j]))
            return ans
        return dfs(s, f) % (10 ** 9 + 7)
