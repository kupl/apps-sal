(n, a, b, *x) = list(map(int, open(0).read().split()))
now = x[0]
ans = 0
for i in range(1, n):
    cost = (x[i] - now) * a
    if cost > b:
        ans += b
    else:
        ans += cost
    now = x[i]
print(ans)
