
MVAL = 1000000007


def rangeand(low, hi):
    ra = 0
    p2 = 1
    while p2 <= low:
        ld, lm = divmod(low, p2 * 2)
        hd, hm = divmod(hi, p2 * 2)
        if ld == hd:
            ra += ((hm - lm + 1) * (p2 & lm)) % MVAL
        else:
            ra += ((p2 * 2 - lm) * (p2 & lm)) % MVAL
        p2 *= 2
    return ra % MVAL


t = int(input())
for ti in range(t):
    l, r = list(map(int, input().split()))

    print(rangeand(l, r))
