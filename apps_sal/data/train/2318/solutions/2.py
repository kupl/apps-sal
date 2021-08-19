(n, k) = map(int, input().split())
(c, v) = (0, [])
for (i, a) in enumerate(map(int, input().split())):
    j = i + 1 - len(v)
    d = c - (j - 1) * (n - j) * a
    if d < k:
        v.append(i + 1)
        n -= 1
    else:
        c += a * (j - 1)
print('\n'.join(map(str, v)))
