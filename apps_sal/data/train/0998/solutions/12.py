(n, q) = map(int, input().split())
g = [0] * n
g1 = [0] * n
while q > 0:
    (o, r, v) = input().split()
    if o == 'RowAdd':
        g[int(r) - 1] += int(v)
    else:
        g1[int(r) - 1] += int(v)
    q = q - 1
print(max(g) + max(g1))
