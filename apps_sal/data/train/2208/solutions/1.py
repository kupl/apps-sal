import sys
input = sys.stdin.readline

from collections import deque
N, K = list(map(int, input().split()))
X = [[] for i in range(N)]
for i in range(K):
    x, y = list(map(int, input().split()))
    X[x-1].append(y-1)
    X[y-1].append(x-1)

mi = 10**6
mii = 0
for i in range(N):
    if len(X) and (len(X) < mi):
        mi = len(X)
        mii = i

Y = [(len(X[i]), i) for i in range(N) if len(X[i])]
Y = sorted(Y)
Q = [y[1] for y in Y]

P = [-1] * N
D = [0] * N
ans = 0
while Q:
    i = Q.pop()
    for a in X[i]:
        if D[a] == 0 or D[i] == 0:
            ans += 1
            D[a] = 1
            D[i] = 1
            if a != P[i]:
                P[a] = i
                X[a].remove(i)
                Q.append(a)
print(K - ans)



