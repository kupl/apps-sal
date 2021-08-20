import math
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    g = math.gcd(a, b)
    res = a * b / (g * g)
    print(int(res))
