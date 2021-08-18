import math

for _ in range(int(input())):
    n, d = list(map(int, input().split(' ')))
    l = list(map(int, input().split(' ')))
    l1 = []
    l2 = []

    for i in l:
        if i >= 80 or i <= 9:
            l1.append(i)
        else:
            l2.append(i)

    x = math.ceil(len(l1) / d)
    y = math.ceil(len(l2) / d)

    print(x + y)
