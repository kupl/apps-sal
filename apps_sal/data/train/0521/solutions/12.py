from math import *
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    l = list(map(int, input().split()))
    arr.sort()
    x = l[0]
    y = l[1]
    ans = 0
    for i in range(int(n / 2)):
        x1 = arr[i]
        x2 = arr[n - i - 1]
        if x1 < x and x2 <= x:
            angle = atan((x - x1) / y) - atan((x - x2) / y)
        elif x1 < x and x2 > x:
            angle = atan((x - x1) / y) + atan((x2 - x) / y)
        else:
            angle = atan((x2 - x) / y) - atan((x1 - x) / y)
        ans += angle
    print(ans)
