N, C = map(int, input().split())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
P = 10**9 + 7
Y = [[pow(i, j, P) for j in range(401)] for i in range(401)]
for i in range(1, 401):
    for j in range(401):
        Y[i][j] = (Y[i][j] + Y[i - 1][j]) % P
X = [[0] * (C + 1) for _ in range(N + 1)]
X[0][0] = 1
for i in range(1, N + 1):
    for j in range(C + 1):
        X[i][j] = sum([X[i - 1][k] * (Y[B[i - 1]][j - k] - Y[A[i - 1] - 1][j - k]) % P for k in range(j + 1)]) % P
print(X[N][C])
