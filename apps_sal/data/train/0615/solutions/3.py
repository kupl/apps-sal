import math
t = int(input())
for ii in range(t):
    n, q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    pre = []
    s = 0
    for i in arr:
        s += i
        pre.append(s)
    for i in range(q):
        l, r = [int(x) for x in input().split()]
        l -= 1
        r -= 1
        if(l == 0):
            print(pre[r])
        else:
            print(pre[r] - pre[l - 1])
