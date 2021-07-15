import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    f = [[a, 0] for a in map(int, input().split())]
    dot = lambda p0, p1 : sorted(p0 + p1, reverse = 1)[:2]

    for i in range(n):
        for U in range(1 << n):
            if not U >> i & 1:
                f[U | 1 << i] = dot(f[U | 1 << i], f[U])

    res = 0
    for i in range(1, 1 << n):
        res = max(res, sum(f[i]))
        print(res)
resolve()
