n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
o = 0.0

for i in range(m):

    x, y, c = list(map(int, input().split()))
    o = max(o, (a[x - 1] + a[y - 1]) / c)

print(o)
