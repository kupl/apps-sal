from math import gcd as g
t = int(input())
while t != 0:
    (n, a, b, k) = map(int, input().split())
    lcm = a * b // g(a, b)
    div_a = n // a - n // lcm
    div_b = n // b - n // lcm
    net = div_a + div_b
    if net >= k:
        print('Win')
    else:
        print('Lose')
    t -= 1
