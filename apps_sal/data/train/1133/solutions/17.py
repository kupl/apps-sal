# cook your dish here
import math
t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    minimum = min(lst)
    x = 1
    xlist = []
    for k in range(1, minimum + 1):
        for j in lst:
            if j % k == 0:
                xlist.append(k)
            else:
                break
    xlist = sorted(xlist, reverse=True)
    for m in xlist:
        if xlist.count(m) == n:
            print(m, math.ceil(sum(lst) / m))
            break
