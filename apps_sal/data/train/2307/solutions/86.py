N, A, B = list(map(int, input().split()))
X = list(map(int, input().split()))

now = X[0]
ans = 0
for x in X:
    ans += min(B, A * (x - now))
    now = x

print(ans)
