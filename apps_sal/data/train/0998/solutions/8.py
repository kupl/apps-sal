n, q = list(map(int, input().split()))
r = [0] * n
c = [0] * n
for _ in range(q):
    s, x, p = list(map(str, input().split()))
    x, p = int(x), int(p)
    if s == 'RowAdd':
        r[x - 1] += p
    else:
        c[x - 1] += p
print(max(r) + max(c))
