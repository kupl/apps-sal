import math
tc = int(input())
for i in range(tc):
    (x, y) = list(map(int, input().split()))
    gcd = math.gcd(x, y)
    lcm = x * y // gcd
    print(gcd, lcm)
