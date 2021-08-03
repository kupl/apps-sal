from math import log
q = int(input())
prix = {}
depenses = []


def est_dessous(v, u):
    return u == v or u == 1 or (u < v and 0 <= v - 2**int(log(v / u) / log(2)) * u < 2**int(log(v / u) / log(2)))


def pqc(u, v):
    # retourne la liste des ARETES empruntées
    res = []
    while not est_dessous(v, u):
        res.append((u, u // 2))
        u = u // 2
    while not u == v:
        if est_dessous(v, 2 * u):
            res.append((u, 2 * u))
            u = 2 * u
        elif est_dessous(v, 2 * u + 1):
            res.append((u, 2 * u + 1))
            u = 2 * u + 1
    return res


for k in range(q):
    event = tuple(map(int, input().split()))
    if event[0] == 1:
        for (a, b) in pqc(event[1], event[2]):
            if (a, b) in prix:
                prix[(a, b)] += event[3]
            elif (b, a) in prix:
                prix[(b, a)] += event[3]
            else:
                prix[(a, b)] = event[3]
    else:
        s = 0
        for (a, b) in pqc(event[1], event[2]):
            if (a, b) in prix:
                s += prix[(a, b)]
            elif (b, a) in prix:
                s += prix[(b, a)]
        depenses.append(s)

for k in depenses:
    print(k)
