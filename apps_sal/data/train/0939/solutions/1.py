import sys
from functools import lru_cache
lucky = {4, 774, 7, 744, 777, 74, 747, 44, 77, 47, 474, 444, 477, 447}
sys.setrecursionlimit(10 ** 6)
mod = 10 ** 9 + 7
fact = [1]
for i in range(1, 1001):
    fact.append(fact[-1] * i % mod)
inv = [pow(i, mod - 2, mod) for i in fact]
def C(k, n): return fact[n] * inv[n - k] * inv[k] % mod


def f(n):
    n = [int(x) for x in n]

    @lru_cache(None)
    def dp(pos, cnt, free):
        if cnt > 777:
            return 0
        diff = len(n) - pos
        ans = 0
        if free:
            for i in lucky:
                i -= cnt
                if 0 <= i <= diff:
                    ans += C(i, diff) * pow(2, i, mod) * pow(8, diff - i, mod)
                    ans %= mod
            return ans
        if pos == len(n):
            return int(cnt in lucky)
        for i in range(10 if free else n[pos] + 1):
            ans += dp(pos + 1, cnt + int(i == 4 or i == 7), free or i < n[pos])
            ans %= mod
        return ans
    return dp(0, 0, 0)


t = int(input())
for _ in range(t):
    l, r = input().split()
    l = str(int(l) - 1)
    print((f(r) - f(l)) % mod)
