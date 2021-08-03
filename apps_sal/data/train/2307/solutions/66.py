n, a, b = map(int, input().split())
xs = list(map(int, input().split()))
s = xs[0]
rt = 0
for i in xs[1:]:
    rt += min(a * (i - s), b)
    s = i
print(rt)
