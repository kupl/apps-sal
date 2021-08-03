n = int(input())
a = list(map(int, input().split()))
l = [(x, i) for i, x in enumerate(a)]
l.sort(reverse=True)
l += [(0, n)]
g = [0] * n
m = n
for i in range(n):
    s = l[i][1]
    if m > s:
        m = s
    g[m] += (l[i][0] - l[i + 1][0]) * (i + 1)
for x in g:
    print(x)
