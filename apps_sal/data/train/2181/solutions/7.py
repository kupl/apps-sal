n = int(input())
p = list(map(int, input().split()))
a = [0] * n
t = 0
for i in range(n):
    if p[i] <= t:
        a[i] = t - p[i] + 1
    t = max(p[i], t + 1)
t = 0
for i in range(n - 1, 0, -1):
    if p[i] <= t:
        a[i] = min(t - p[i] + 1, a[i])
    else:
        a[i] = 0
    t = max(p[i], t + 1)
f = 0
for i in range(n):
    p[i] += a[i]
    f |= i > 1 and p[i] == p[i - 1]
print(sum(a[1:n - 1]) + f)
