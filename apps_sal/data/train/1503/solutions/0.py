import math
N = int(input())
for i in range(N):
    a, b = list(map(int, input().split()))
    c = a // math.gcd(a, b) * b // math.gcd(a, b)
    print(c)
