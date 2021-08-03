from math import gcd
for ii in range(int(input())):
    N = int(input())
    N *= 24
    X = input().split()
    x, y, z = int(X[0]), int(X[1]), int(X[2])

    a = [x, y, z]
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)

    print(N // lcm)
