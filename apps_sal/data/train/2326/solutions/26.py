n = int(input())
a = [0] + list(map(int, input().split()))
p = sorted(((-a[i], -i) for i in range(n + 1)))
ans = [0] * (n + 1)
m = n
for i in range(n):
    (k, v) = (-p[i][1], -p[i][0])
    nv = -p[i + 1][0]
    m = min(m, k)
    ans[m] += (i + 1) * (v - nv)
print(*ans[1:], sep='\n')
