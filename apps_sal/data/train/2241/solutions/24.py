N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Mod = 10**9 + 7

B_max = max(B)
P = [[0] * (C + 1) for _ in range(B_max + 1)]

for x in range(B_max + 1):
    E = P[x]
    E[0] = 1
    t = 1
    for k in range(1, C + 1):
        E[k] = t = (t * x) % Mod

T = []
for i in range(N):
    U = [0] * (C + 1)
    for x in range(A[i], B[i] + 1):
        for k in range(C + 1):
            U[k] += P[x][k]
            U[k] %= Mod
    T.append(U)

P = [1] + [0] * C
for Q in T:
    X = [0] * (C + 1)

    for i in range(C + 1):
        for j in range(C + 1):
            if i + j > C:
                break
            X[i + j] += P[i] * Q[j]
            X[i + j] %= Mod
    P = X.copy()

print(X[C])
