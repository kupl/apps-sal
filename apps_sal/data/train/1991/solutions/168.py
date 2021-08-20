class Solution:

    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def f(i, fu):
            res = int(i == finish)
            for (j, p) in enumerate(A):
                d = abs(p - A[i])
                if j != i and d <= fu:
                    res = (res + f(j, fu - d)) % MOD
            return res
        return f(start, fuel) % MOD
