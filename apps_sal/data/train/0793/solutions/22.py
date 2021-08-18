import math

n, r = list(map(int, input().split()))


def gcd(l):
    m = math.gcd(l[0], l[1])
    for t in l[2:]:
        m = math.gcd(m, t)
    return m


l = list(int(i) for i in input().split())
l1 = list([abs(x - r) for x in l])
print(gcd(l1))
