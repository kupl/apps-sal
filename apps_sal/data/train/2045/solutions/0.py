n, m = map(int, input().split())
p, d = [0] * (n + 2), [0] * (n + 2)
for i in range(m):
    l, r, x = map(int, input().split())
    while l < x:
        if d[l]:
            k = d[l]
            d[l] = x - l
            l += k
        else:
            d[l], p[l] = x - l, x
            l += 1
    l += 1
    r += 1
    while d[r]: r += d[r]
    while l < r:
        if d[l]:
            k = d[l]
            d[l] = r - l
            l += k
        else:
            d[l], p[l] = r - l, x
            l += 1
print(' '.join(map(str, p[1: -1])))
