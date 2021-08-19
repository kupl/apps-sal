(n, m) = map(int, input().split())
(p, mem) = (3, [])
res = 2 ** n - 2
if n % 2 == 0:
    res -= 2
while p < n:
    if not any((p % e == 0 for e in mem)) and n % p == 0:
        mem.append(p)
        res -= 2 ** p - 2
    p += 2
print(res % m)
