# https://www.codechef.com/problems/RGAND

MVAL = 1000000007


def rangeand(low, hi):
    ra = 0
    p2 = 1
    lmd = 0
    ldv = low
    hdv = hi
    while p2 <= low:
        thisbit = low & p2
        p2 *= 2
        ldv //= 2
        hdv //= 2
        if ldv == hdv:
            ra += ((hi + 1 - low) * (low - lmd)) % MVAL
            break
        elif thisbit > 0:
            lmd += thisbit
            ra += ((p2 - lmd) * thisbit) % MVAL
    return ra % MVAL


t = int(input())
for ti in range(t):
    l, r = list(map(int, input().split()))

    print(rangeand(l, r))
