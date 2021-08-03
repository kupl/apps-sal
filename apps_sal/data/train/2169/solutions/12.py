n, p, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    now = a[i] * a[i] * a[i] * a[i] - k * a[i]
    now %= p
    if now in d:
        d[now] += 1
    else:
        d[now] = 1
ans = 0
for i in range(n):
    now = a[i] * a[i] * a[i] * a[i] - k * a[i]
    now %= p
    ans += d[now] - 1
ans //= 2
print(ans)
