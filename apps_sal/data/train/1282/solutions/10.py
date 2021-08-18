
MVAL = 1000000007


def rangeand(low, hi):
    odf = hi - low + 1
    ra = 0
    p2 = 1
    lmd = 0
    while (low & p2) == 0:
        p2 *= 2
    pmdf = p2
    if pmdf >= odf:
        return (odf * low) % MVAL
    while p2 <= low:
        if (low & p2):
            lmd += p2
            ra += (pmdf * p2) % MVAL
        else:
            pmdf += p2
            if pmdf >= odf:
                ra += (odf * (low - lmd)) % MVAL
                break
        p2 *= 2

    return ra % MVAL


t = int(input())
ans = []
for ti in range(t):
    l, r = map(int, input().split())

    ans.append(rangeand(l, r))

print(*ans, sep='\n')
