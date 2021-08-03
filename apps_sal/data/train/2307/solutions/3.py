N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = B * (N - 1)
tmp = 0
for i in range(N - 1):
    tmp += min(A * (X[i + 1] - X[i]), B)
ans = min(ans, tmp)
print(ans)
