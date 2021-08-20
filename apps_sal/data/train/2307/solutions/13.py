(N, A, B) = map(int, input().split())
X = list(map(int, input().split()))
n0 = B // A
S = 0
for i in range(N - 1):
    if X[i + 1] - X[i] <= n0:
        S += (X[i + 1] - X[i]) * A
    else:
        S += B
print(S)
