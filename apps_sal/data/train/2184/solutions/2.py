(N, Q) = list(map(int, input().split()))
A = [int(a) for a in input().split()]
B = sorted(list(set(A)))
M = len(B)
IA = {}
for i in range(M):
    IA[B[i]] = i
A = [IA[a] for a in A]
L = [N] * M
R = [-1] * M
C = [0] * M
for i in range(N):
    L[A[i]] = min(L[A[i]], i)
    R[A[i]] = max(R[A[i]], i)
    C[A[i]] += 1
X = []
for i in range(M):
    X.append((L[i], R[i], C[i]))
X = sorted(X, key=lambda x: x[1])
Y = [(-1, 0, 0)]
for i in range(M):
    (l, r, t) = X[i]
    m = t
    while Y[-1][0] > l:
        (a, b, c) = Y.pop()
        t += b
        m = max(m, c)
    Y.append((r, t, m))
print(sum([y[1] - y[2] for y in Y[1:]]))
