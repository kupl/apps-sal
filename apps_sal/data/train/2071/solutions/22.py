q = {}
w = {}
e = {}
r = 0
for _ in range(int(input())):
    (x, y) = map(int, input().split())
    (a, s, d) = (q.get(x, 0), w.get(y, 0), e.get((x, y), 0))
    r += a + s - d
    (q[x], w[y], e[x, y]) = (a + 1, s + 1, d + 1)
print(r)
