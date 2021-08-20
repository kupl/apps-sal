(n, m) = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for t in range(m):
    (x, y, c) = map(int, input().split())
    ans = max(ans, (l[x - 1] + l[y - 1]) / c)
print(ans)
