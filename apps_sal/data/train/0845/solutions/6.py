import math
n = int(input())
for i in range(n):
    c = list(map(int, input().split()))
    d = math.gcd(c[0], c[1])
    h = int((c[0] * c[1]) / (d**2))
    print(h)
