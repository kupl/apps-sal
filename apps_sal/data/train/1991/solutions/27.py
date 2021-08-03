from functools import lru_cache as l


class Solution:
    def countRoutes(self, a: List[int], s: int, t: int, fuel: int) -> int:
        # d = [x:i for i,x in enumerate(a)]
        n = len(a)

        @l(None)
        def dp(i, f):
            if f < 0:
                return 0

            # cur = a[i]
            ans = 0
            if i == t:
                ans += 1
            for j in range(n):
                if j != i:
                    ans += dp(j, f - abs(a[i] - a[j]))
            return ans

        return (dp(s, fuel) % (10**9 + 7))
