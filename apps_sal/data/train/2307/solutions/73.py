N, A, B = map(int, input().split())
*X, = map(int, input().split())
i = 1
ans = 0
while i < N:
    ans += min(B, A * (X[i] - X[i - 1]))
    i += 1
print(ans)
