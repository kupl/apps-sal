# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    x = (-1 + (8*n + 9)**0.5)*0.5
    ans = n - math.ceil(x) + 1
    print(ans)
