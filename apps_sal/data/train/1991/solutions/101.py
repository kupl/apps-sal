class Solution:

    def countRoutes(self, arr: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def f(curr, fu):
            ans = int(curr == finish)
            for i in range(n):
                if i != curr:
                    if abs(arr[i] - arr[curr]) <= fu:
                        ans += f(i, fu - abs(arr[i] - arr[curr]))
                        ans %= mod
            return ans
        return f(start, fuel)
