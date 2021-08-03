from math import sqrt as S


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    n = int(input())
    tot = n * n
    s = 0
    beta = int(S(n))
    for i in range(1, int(S(n)) + 1):
        s += n // i
    s = 2 * s - beta * beta
    g = gcd(s, tot)
    s = s // g
    tot = tot // g
    print(s, end='')
    print('/', end='')
    print(tot)
