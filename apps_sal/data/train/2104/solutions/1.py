n = int(input())
v = sorted([int(x) for x in input().split()])
ans = (v[n - 1] - v[0]) * (v[n * 2 - 1] - v[n])
for i in range(1, n + 1) :
    ans = min(ans, (v[i + n - 1] - v[i]) * (v[2 * n - 1] - v[0]))
print(ans)

