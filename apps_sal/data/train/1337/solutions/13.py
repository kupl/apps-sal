from math import gcd
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    r = int(input())
    lcm = p[0]
    for i in p[1:]:
        lcm = int(lcm * i / gcd(lcm, i))
    print(int(lcm + r))
