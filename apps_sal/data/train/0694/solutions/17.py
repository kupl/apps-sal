import math


def compute_lcm(x, y):
    return x * y // math.gcd(x, y)


T = int(input())
for i in range(T):
    N = int(input())
    (x, y, z) = list(map(int, input().strip().split()))
    lcm = compute_lcm(compute_lcm(x, y), z)
    print(N * 24 // lcm)
