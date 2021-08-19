(n, m) = list(map(int, input().split()))
gr = [set() for i in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    gr[a - 1].add(b - 1)
    gr[b - 1].add(a - 1)
v = [False for i in range(n)]
an = 0
for i in range(n):
    if v[i]:
        continue
    s = [i]
    d = 0
    v[i] = True
    while s:
        x = s.pop()
        d += 1
        for j in gr[x]:
            if v[j]:
                continue
            v[j] = True
            s.append(j)
    an += d - 1
print(m - an)
