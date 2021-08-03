import math
for i in range(int(input())):
    y = int(input())
    x = list(map(int, input().split()))
    p = 1
    for j in x:
        p = p * j

    m = max(x)

    r = 1

    for k in range(2, m):

        if p % k**2 == 0:
            r = k
            break
    print(r)
