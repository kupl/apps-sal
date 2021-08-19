# cook your dish here
import math
t = int(input())
while t > 0:
    n, l = list(map(int, input().split()))
    if n == 1:
        print(l)
    elif n == 2:
        ans = 0
        while l > 0:
            ans += 1
            l = l // 2
        print(ans)

    t -= 1
