import math
def survivor(zombies):
    if zombies == []:
        return -1
    if do_gcd(zombies) !=1:
        return -1
    if min(zombies) == 1:
        return 0
    if len(zombies) == 2:
        return do_lcm(zombies) - sum(zombies)
    a = sorted(zombies)
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
            for q in range(a1):
                if (q % d) == r:
                    nn = min(nn, n[q])
            if nn < inf:
                for j in range(int(a1/d) - 1):
                    nn = nn + a[i]
                    p = nn % a1
                    nn = min(nn, n[p])
                    n[p] = nn
    return max(n) - a1

def do_gcd(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return math.gcd(array[0], array[1])
    return math.gcd(array[0], do_gcd(array[1:]))

def do_lcm(array):
    return int(array[0]*array[1]/math.gcd(array[0], array[1]))
