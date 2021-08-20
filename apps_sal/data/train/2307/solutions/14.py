(N, A, B) = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()
ans = 0
for i in range(1, N):
    ans += min((X[i] - X[i - 1]) * A, B)
print(ans)
