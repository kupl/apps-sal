import math


def min_price(coins):
    if coins == []:
        return -1
    if do_gcd(coins) != 1:
        return -1
    if min(coins) == 1:
        return 1
    if len(coins) == 2:
        return do_lcm(coins) - sum(coins) + 1
    a = sorted(coins)
    a1 = a[0]
    k = len(a)
    inf = math.inf
    n = [0]
    for i in range(1, a1):
        n.append(inf)
    for i in range(1, k):
        d = math.gcd(a1, a[i])
        for r in range(d):
            nn = inf
            for q in range(r, a1, d):
                if (q % d) == r:
                    nn = min(nn, n[q])
            if nn < inf:
                for j in range(int(a1 / d) - 1):
                    nn = nn + a[i]
                    p = nn % a1
                    nn = min(nn, n[p])
                    n[p] = nn
    return max(n) - a1 + 1


def do_gcd(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return math.gcd(array[0], array[1])
    return math.gcd(array[0], do_gcd(array[1:]))


def do_lcm(array):
    return int(array[0] * array[1] / math.gcd(array[0], array[1]))
