v0 = 0
l = []
(n, m) = (int(x) for x in input().split())
for i in range(n):
    l2 = []
    curs = set([int(x) for x in input().split()][1:])
    if not curs:
        v0 += 1
        continue
    for s in l:
        if curs & s:
            curs |= s
        else:
            l2.append(s)
    l2.append(curs)
    l = l2
print(v0 + max(0, len(l) - 1))
