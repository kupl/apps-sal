# cook your dish here
t = int(input())
MOD = 1000000007


def mod(n, m=MOD):
    n %= m
    while n < 0:
        n += m
    return n


def power(n, p):
    res = 1
    while p:
        if p % 2:
            res = mod(res * n)
        p //= 2
        n = mod(n * n)
    return res


while t:
    ma = input().split()
    x = int(ma[0])
    y = int(ma[1])
    s = int(ma[2])
    ma = input().split()
    u = int(ma[0])
    v = int(ma[1])
    if s % x == 0 and ((s // x) & ((s // x) - 1) == 0):
        inv = power(u, MOD - 2)
        print(mod(mod(mod(s // x) * v) * inv))
    else:
        inv = power(v - u, MOD - 2)
        print(mod(mod(mod(s // y) * v) * inv))
    t -= 1
