n, a, b = list(map(int, input().split()))
X = list(map(int, input().split()))
p = X[0]
ans = 0
for x in X[1:]:
    d = x - p
    if d * a <= b:
        ans += d * a
    else:
        ans += b
    p = x
print(ans)
