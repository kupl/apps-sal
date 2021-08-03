from math import gcd


def compute_lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm


def LCMofArray(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // gcd(lcm, a[i])
    return lcm


for _ in range(int(input())):
    lens = int(input())
    arrs = [int(x) for x in input().split()]
    rest = int(input())
    print(LCMofArray(arrs) + rest)
