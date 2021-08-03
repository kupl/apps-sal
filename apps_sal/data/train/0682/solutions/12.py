from sys import stdin, stdout, exit
from heapq import *
try:
    n = (int(stdin.readline()))
    a = list(map(int, stdin.readline().split()))
    s = 0
    l = 0
    r = n
    left = right = False
    for i in range(n):
        if s + 1 == a[i]:
            s = a[i]
        else:
            l = i
            s = a[l]
            break
    for i in range(l + 1, n):
        if s - 1 == a[i]:
            s = a[i]
        else:
            s = a[i]
            r = i
            break
    arr = a[:l] + (a[l:r])[::-1] + a[r:]
    s = 0
    ans = True
    for i in arr:
        if s + 1 == i:
            s = i
        else:
            ans = False
            break
    if ans and l + 1 != r:
        print(l + 1, r)
    else:
        print(0, 0)
except:
    print(0, 0)
