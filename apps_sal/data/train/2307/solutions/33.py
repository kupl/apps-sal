(N, A, B) = list(map(int, input().split()))
X = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    d = X[i] - X[i - 1]
    ans += min(d * A, B)
print(ans)
