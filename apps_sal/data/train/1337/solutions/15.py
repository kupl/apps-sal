from math import gcd
for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    R = int(input())
    lcm = lst[0]

    for i in lst[1:]:
        lcm = lcm * (i // (gcd(lcm, i)))
    print(lcm + R)
