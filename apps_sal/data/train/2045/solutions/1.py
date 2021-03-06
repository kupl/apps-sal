(n, m) = map(int, input().split())
(p, d) = ([0] * (n + 2), list(range(1, n + 3)))
for i in range(m):
    (l, r, x) = map(int, input().split())
    while l < x:
        if p[l]:
            k = d[l]
            d[l] = x
            l = k
        else:
            (d[l], p[l]) = (x, x)
            l += 1
    l += 1
    r += 1
    while p[r]:
        r = d[r]
    while l < r:
        if p[l]:
            k = d[l]
            d[l] = r
            l = k
        else:
            (d[l], p[l]) = (r, x)
            l += 1
print(' '.join(map(str, p[1:-1])))
