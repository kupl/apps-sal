import sys
read = sys.stdin.read
(n, *A) = map(int, read().split())
S = sorted([(a, i) for (i, a) in enumerate(A)], reverse=True)
(X, Y) = zip(*S)
m = 10 ** 9
L = [0] * n
for (i, y) in enumerate(Y):
    m = min(m, y)
    if i == n - 1:
        L[m] += (i + 1) * X[i]
    else:
        L[m] += (i + 1) * (X[i] - X[i + 1])
print(*L, sep='\n')
