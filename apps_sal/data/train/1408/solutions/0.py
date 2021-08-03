from collections import Counter
mod = 10 ** 9 + 7
choice = {'1': ['11', '21', '22'], '2': ['11', '12', '21']}


def solve(a, b):
    n = len(a)
    if n == 1:
        return 2
    dp = Counter([('11', '11')])
    for i in range(n - 1):
        new = Counter()
        for x, y in (a[i], b[i]), (b[i], a[i]):
            for p in choice[x]:
                for q in choice[y]:
                    m = p[-1] + x
                    n = q[-1] + y
                    new[m, n] += dp[p, q]
                    new[m, n] %= mod
        dp = new
    ans = 0
    for i in '11', '21', :
        for j in '11', '21':
            ans += dp[i, j]
    return (ans * 2) % mod


t = int(input())
for _ in range(t):
    a = input()
    b = input()
    print(solve(a, b))
