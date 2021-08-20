(N, A, B) = map(int, input().split())
X = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    if (X[i] - X[i - 1]) * A < B:
        ans += (X[i] - X[i - 1]) * A
    else:
        ans += B
print(ans)
