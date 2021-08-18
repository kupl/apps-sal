import math
t = int(input())
for i in range(t):
    l, b = map(int, input().split())
    area = l * b
    gcd = math.gcd(l, b)
    gcd = gcd**2
    print(area // gcd)
