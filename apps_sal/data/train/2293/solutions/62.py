def max2(p, q):
    (e, b) = (p[0], p[1])
    (c, d) = (q[0], q[1])
    s = list(set([e, b, c, d]))
    (m1, m2) = (1 << n, 1 << n)
    for i in s:
        if a[m1] < a[i]:
            m2 = m1
            m1 = i
        elif a[m2] < a[i]:
            m2 = i
    return (m1, m2)


n = int(input())
a = list(map(int, input().split()))
g = [(i, 1 << n) for i in range(1 << n)]
a += [0]
res = 0
for i in range(n):
    for j in range(1 << n):
        if 1 << i & j:
            g[j] = max2(g[j], g[j ^ 1 << i])
ans = []
for i in range(1, 1 << n):
    res = max(res, a[g[i][0]] + a[g[i][1]])
    ans.append(res)
print(*ans, sep='\n')
