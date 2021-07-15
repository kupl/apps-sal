n, m = map(int, input().split())
t, v = 0, [0] + list(map(int, input().split()))
for i in range(m):
    x, y, d = map(int, input().split())
    t = max(t, (v[x] + v[y]) / d)
print(t)
