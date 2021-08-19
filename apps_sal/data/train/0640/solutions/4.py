# cook your dish here
import math
t = int(input())
for i in range(t):
    x, y = list(map(int, input().split()))
    if x != y:
        l = x * y // math.gcd(x, y)
        a = (l // x) - 1
        b = (l // y) - 1
        print(a + b)
    else:
        print(0)
