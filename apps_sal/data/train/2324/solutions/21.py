import sys
sys.setrecursionlimit(2 * 10 ** 5)
N = int(input())
(a, b) = list(zip(*(list(map(int, input().split())) for _ in range(N - 1)))) if N - 1 else ((), ())
G = [set() for _ in range(N + 1)]
for (x, y) in zip(a, b):
    G[x].add(y)
    G[y].add(x)
dp = [0 for _ in range(N + 1)]
dp[1] = 1


def f(i):
    for j in G[i]:
        if dp[j] == 0:
            dp[j] = i
            f(j)


f(1)
p = []
i = N
while i != 1:
    p.append(i)
    i = dp[i]
p.append(1)
dp2 = [0 for _ in range(N + 1)]
for j in range(len(p)):
    if dp2[p[-(j + 1)]] == 0:
        dp2[p[-(j + 1)]] = 1
    if dp2[p[j]] == 0:
        dp2[p[j]] = -1
dp3 = [0 for _ in range(N + 1)]
dp3[1] = 1


def g(i):
    for j in G[i]:
        if dp3[j] == 0 and dp2[j] != -1:
            dp3[j] = 1
            g(j)


g(1)
ans = 'Fennec' if dp3.count(1) > N // 2 else 'Snuke'
print(ans)
