import math
T = int(input())
for i in range(T):
    (n, a, b, k) = list(map(int, input().split()))
    lcm = a * b // math.gcd(a, b)
    div_a = n // a - n // lcm
    div_b = n // b - n // lcm
    net = div_a + div_b
    if net >= k:
        print('Win')
    else:
        print('Lose')
