# t=int(raw_input())
import math
t = eval(input())
while t:
    str = input()
    a, b, r = str.split()
    a = int(a)
    b = int(b)
    r = int(r)
    # print(a,b,r)
    # b=input()
    # r=input()
    t = t - 1
    m = min(a, b)
    max_can_remove = (r * (r + 1)) / 2
    ans = 0
    if max_can_remove > m:
        ans = abs(a - b)
    else:
        ans = a + b - (2 * max_can_remove)
    print(ans)
