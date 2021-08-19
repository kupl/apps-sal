import math
for i in range(int(input())):
    y = int(input())
    x = list(map(int, input().split()))
    pr = 1
    for j in x:
        pr = pr * j
    m = max(x)
    rm = 1
    for k in range(2, m):
        if pr % k ** 2 == 0:
            rm = k
            break
    print(rm)
