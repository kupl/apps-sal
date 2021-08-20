N = int(input())
A = [int(a) for a in input().split()]
X = [-1] * (N + 1)
k = 2
while k <= N:
    X[k] = 1
    for i in range(k * 2, N + 1, k):
        X[i] = 0
    while k <= N and X[k] >= 0:
        k += 1
P = [i for i in range(N + 1) if X[i] == 1]
s = sum(A)
L = []
for p in P:
    if s % p == 0:
        L.append(p)
if len(L) == 0:
    print(-1)
else:
    mi = 1 << 100
    for m in L:
        mm = m // 2
        k = 0
        ans = 0
        for i in range(N):
            if A[i]:
                k = (k + 1) % m
            if k <= mm:
                ans += k
            elif k == mm and A[i]:
                pass
            else:
                ans += m - k
        mi = min(mi, ans)
    print(mi)
