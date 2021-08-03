n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(m):
    ax, bx, x = map(int, input().split())
    ans = max(ans, (a[ax - 1] + a[bx - 1]) / x)
print(ans)
