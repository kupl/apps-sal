n, m = map(int, input().split())
an = [int(x) for x in input().split()]
am = [int(x) for x in input().split()]
r = n + m - 1
c = 0
man = an.index(max(an))
for i in range(m):
    print(man, i)
mam = am.index(min(am))
for j in range(n):
    if j == man:
        continue
    print(j, mam)
