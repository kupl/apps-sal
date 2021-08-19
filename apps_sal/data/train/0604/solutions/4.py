import math
t = int(input())
for i in range(t):
    (r, c) = list(map(int, input().split()))
    res = []
    for j in range(r):
        l = list(map(int, input().split()))
        res.append(l)
    flag = 1
    for a in range(r):
        for b in range(c):
            adj = 4
            if a == 0 or a == r - 1:
                adj -= 1
            if b == 0 or b == c - 1:
                adj -= 1
            if res[a][b] >= adj:
                flag = 0
                break
    if flag:
        print('Stable')
    else:
        print('Unstable')
