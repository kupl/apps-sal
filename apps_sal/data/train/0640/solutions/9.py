def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)


itr = int(input())
for _ in range(itr):
    val = list(map(int, input().split()))
    a = val[0]
    b = val[1]
    l = lcm(a, b)
    f = l / a - 1
    s = l / b - 1
    print(int(f + s))
