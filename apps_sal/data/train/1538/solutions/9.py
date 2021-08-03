import math
n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    x = math.gcd(a, b)
    y = (a * b) // x
    print(x, y)
