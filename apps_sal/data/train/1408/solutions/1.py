from collections import Counter
mod = 10 ** 9 + 7


def solve(a, b):
    n = len(a)
    if n == 1:
        return 2
    dp = Counter([('11', '11')])
    for i in range(n - 1):
        new = Counter()
        for p in ('11', '12', '21', '22'):
            for q in ('11', '12', '21', '22'):
                for (x, y) in ((a[i], b[i]), (b[i], a[i])):
                    if x == '2' and p == '22' or (y == '2' and q == '22'):
                        continue
                    if x == '1' and p == '12' or (y == '1' and q == '12'):
                        continue
                    m = p[-1] + x
                    n = q[-1] + y
                    new[m, n] += dp[p, q]
                    new[m, n] %= mod
        dp = new
    ans = 0
    for i in ('11', '21'):
        for j in ('11', '21'):
            ans += dp[i, j]
    return ans * 2 % mod


t = int(input())
for _ in range(t):
    a = input()
    b = input()
    print(solve(a, b))
