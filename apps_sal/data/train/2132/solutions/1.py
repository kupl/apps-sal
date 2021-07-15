import sys
input = sys.stdin.readline
MOD = 998244353
fa = [1]
for i in range(1, 2*10**5+10):
    fa.append(fa[-1]*i%MOD)

N = int(input())
X = [[] for i in range(N)]
for i in range(N-1):
    x, y = list(map(int, input().split()))
    X[x-1].append(y-1)
    X[y-1].append(x-1)

P = [-1] * N
Q = [0]
while Q:
    i = Q.pop()
    for a in X[i]:
        if a != P[i]:
            P[a] = i
            X[a].remove(i)
            Q.append(a)

ans = N
for i in range(len(X)):
    ans = ans * fa[len(X[i])+(1 if i else 0)] % MOD
print(ans)

