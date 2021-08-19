import bisect
(n, t) = list(map(int, input().split()))
a = list(map(int, input().split()))
mx = 0
p = [0] * n
for i in range(n - 1, -1, -1):
    mx = max(mx, a[i])
    p[i] = mx - a[i]
p.sort()
print(n - bisect.bisect_left(p, p[-1]))
