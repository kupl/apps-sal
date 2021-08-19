import math
for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    d = list(map(int, input().split()))[:a]
    l1 = []
    l2 = []
    for i in range(len(d)):
        if d[i] >= 80 or d[i] <= 9:
            l1.append(d[i])
        else:
            l2.append(d[i])
    r1 = math.ceil(len(l1) / b)
    r2 = math.ceil(len(l2) / b)
    print(r1 + r2)
