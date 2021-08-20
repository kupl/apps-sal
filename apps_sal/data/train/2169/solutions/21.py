(n, p, k) = map(int, input().split())
a = list(map(int, input().split()))
d = {}
for x in a:
    v = (x ** 4 - k * x) % p
    if v < p:
        v += p
    if v not in d:
        d[v] = 1
    else:
        d[v] += 1
s = 0
for v in d.values():
    s += v * (v - 1) // 2
print(s)
