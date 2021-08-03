import math

# function to calculate LCM


def L(a):
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    return lcm


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    r = int(input())
    c = L(l)
    print(c + r)
