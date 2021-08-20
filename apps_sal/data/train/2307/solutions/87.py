(N, A, B) = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = [0] * (N - 1)
for i in range(N - 1):
    Y[i] = X[i + 1] - X[i]
out = 0
for i in range(N - 1):
    out += min(B, Y[i] * A)
print(out)
