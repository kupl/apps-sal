(n, t) = list(map(int, input().split()))
a = list(map(int, input().split()))
pos = {}
mx = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    mx[i] = max(mx[i + 1], a[i])
for i in range(n):
    pos[a[i]] = i
a.sort()
ans = 0
b = 0
for i in range(n):
    idx = pos[a[i]]
    if b < mx[idx] - a[i]:
        b = mx[idx] - a[i]
        ans = 1
    elif b == mx[idx] - a[i]:
        ans += 1
print(ans)
