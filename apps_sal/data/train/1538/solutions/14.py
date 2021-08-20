import math
N = int(input())
for i in range(N):
    (a, b) = list(map(int, input().split()))
    c = math.gcd(a, b)
    lcm = a * b // c
    print(c, lcm)
