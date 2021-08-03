import math
t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    x = math.gcd(a, b)
    m = ((a * b) // (x**2))
    print(m)
