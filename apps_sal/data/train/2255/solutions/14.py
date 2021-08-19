(n, d, curr) = (int(input()), {(0, 1): 1}, 0)
for (i, e) in enumerate(map(int, input().split())):
    curr ^= e
    p = (curr, i & 1)
    d[p] = d.get(p, 0) + 1
res = sum((n * (n - 1) // 2 for n in list(d.values())))
print(res)
