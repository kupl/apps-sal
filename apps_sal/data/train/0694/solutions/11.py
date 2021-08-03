from sys import stdin
from math import gcd

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    x, y, z = list(map(int, stdin.readline().split()))
    lcm1 = (x * y) // gcd(x, y)
    lcm2 = (lcm1 * z) // gcd(lcm1, z)
    total = 24 * n
    print(total // lcm2)
