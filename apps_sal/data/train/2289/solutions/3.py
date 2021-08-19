import sys


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7
S = input()
N = len(S)
nxt = list2d(N + 1, 26, N)
for i in range(N - 1, -1, -1):
    for c in range(26):
        nxt[i][c] = nxt[i + 1][c]
    c = ord(S[i]) - 97
    nxt[i][c] = i
dp = [INF] * (N + 1)
rest = [None] * (N + 1)
dp[N] = 1
for i in range(N - 1, -1, -1):
    for c in range(26):
        if nxt[i][c] == N:
            if dp[i] > 1:
                dp[i] = 1
                rest[i] = (c, N)
        elif dp[i] > dp[nxt[i][c] + 1] + 1:
            dp[i] = dp[nxt[i][c] + 1] + 1
            rest[i] = (c, nxt[i][c] + 1)
i = 0
ans = []
while i < N:
    (c, idx) = rest[i]
    ans.append(chr(c + 97))
    i = idx
print(''.join(ans))
