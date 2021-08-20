from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 6)


def fn(pos, consecutive):
    if pos >= n:
        return 0
    if (pos, consecutive) in dp:
        return dp[pos, consecutive]
    take_cur = 0
    if consecutive + 1 < 3:
        take_cur = a[pos] + fn(pos + 1, consecutive + 1)
    dp[pos, consecutive] = max(take_cur, fn(pos + 1, 0))
    return dp[pos, consecutive]


for _ in range(1):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dp = {}
    print(fn(0, 0))
