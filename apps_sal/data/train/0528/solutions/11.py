# cook your dish here
import math
t = int(input())
while t > 0:
    n, l = list(map(int, input().split()))
    if n == 1:
        print(l)
    elif n == 2:
        ans = n * 2
        print(ans)

    t -= 1
