import math


def factor_x(m, n):
    res = 0
    st = 0
    for i in range(2, n + 1):
        if n % i == 0:
            st = 0
            st = math.pow(i, m)
            res = res + st
    return res


def factor_k(m, n):
    res = 0
    st = 0
    for i in range(2, n + 1):
        if n % i == 0:
            st = 0
            st = i * m
            res = res + st
    return res


x_fac = 0
k_fac = 0
cycle = int(input())
cy = 0
while cy < cycle:
    (x, k) = input().split()
    (x, k) = (int(x), int(k))
    x_fac = factor_x(k, x)
    k_fac = factor_k(x, k)
    print(int(x_fac), ' ', int(k_fac))
    x_fac = 0
    k_fac = 0
    cy = cy + 1
