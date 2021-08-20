from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def fn(pos):
    if pos >= n:
        return 0
    if pos in dp:
        return dp[pos]
    dp[pos] = a[pos] + min(fn(pos + 1), fn(pos + 2), fn(pos + 3))
    return dp[pos]


for _ in range(1):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dp = {}
    if n <= 2:
        print(min(a))
        continue
    print(min(fn(0), fn(1), fn(2)))
