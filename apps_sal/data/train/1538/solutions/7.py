import math
for t in range(int(input())):
    (a, b) = map(int, input().split())
    x = math.gcd(a, b)
    y = a * b // x
    print(x, y)
