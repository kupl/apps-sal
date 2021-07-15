n, m = map(int, input().split())
e = set(tuple(map(int, input().split())) for _ in range(m))
a = set(range(1, n + 1))
q = []
r = 0
while a:
    if q:
        u = q.pop()
    else:
        u = a.pop()
        r += 1
    c = {v for v in a if (u, v) not in e and (v, u) not in e}
    a -= c
    q += c
print(r - 1)
