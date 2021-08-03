# cook your dish here

import math


def a(n):
    x = math.ceil(n / 2)
    e = 1000000007
    c = pow(25, e - 2, e)
    if n % 2 == 0:
        a = (pow(26, x, e) - 1) % e
        ans = (2 * a * 26 * c) % e
    else:
        if x == 1:
            ans = 26
        else:
            a = (pow(26, x - 1, e) - 1) % e
            ans = (2 * a * 26 * c) % e
            ans = (ans + pow(26, x, e)) % e
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    print(a(n))
