(n, k) = list(map(int, input().split()))
(c, m, l, r) = (0, 0, [], 0)
for e in [int(i) for i in input().split()]:
    d = m - c * (n - c - 1) * e
    r += 1
    if d < k:
        n -= 1
        l += [r]
    else:
        m += c * e
        c += 1
l.sort()
for e in l:
    print(e)
