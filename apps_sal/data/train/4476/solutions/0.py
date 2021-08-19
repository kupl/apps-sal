from bisect import bisect_left as bisect
n = 5000000
(sieve, PED, PED_DATA) = ([0] * ((n >> 1) + 1), [], [])
for i in range(3, n + 1, 2):
    if not sieve[i >> 1]:
        for j in range(i ** 2 >> 1, n + 1 >> 1, i):
            sieve[j] = 1
        s = str(i)
        nEveD = sum((s.count(d) for d in '02468'))
        if nEveD:
            PED.append(i)
            PED_DATA.append((nEveD, len(s) - 1))


def f(n):
    idx = bisect(PED, n) - 1
    (m, (nEveD, l)) = (PED[idx], PED_DATA[idx])
    for c in range(idx):
        (mc, (nEveDc, lc)) = (PED[idx - c], PED_DATA[idx - c])
        if nEveDc > nEveD:
            (m, nEveD) = (mc, nEveDc)
        if lc < nEveD:
            break
    return m
