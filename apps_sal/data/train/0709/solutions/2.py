from math import gcd
st = ''


def func(n, l1):
    if n == 1:
        return l1[0]
    elif n == 2:
        return gcd(l1[0], l1[1])
    p = l1[0]
    m = p
    for i in range(1, n):
        g = gcd(p, l1[i])
        m = max(m, g)
        p = g
    p = l1[-1]
    m = max(m, p)
    for i in range(n - 2, 0, -1):
        g = gcd(l1[i], p)
        m = max(m, g)
        p = g
    return m


for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    st += str(func(n, l1)) + '\n'

print(st)
'''

'''
