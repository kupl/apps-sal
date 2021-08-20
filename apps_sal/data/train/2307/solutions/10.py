(n, a, b) = map(int, input().split())
X = list(map(int, input().split()))
dist = []
for i in range(n - 1):
    dist.append(X[i + 1] - X[i])
ans = 0
for d in dist:
    if d * a > b:
        ans += b
    else:
        ans += d * a
print(ans)
