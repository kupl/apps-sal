import math
for t in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = sum(a[:m])
    flag = 1
    for i in range(m, n):
        s -= math.ceil(a[i] / 2)
        if (s < 0):
            flag = 0
    if (flag == 1):
        print("VICTORY")
    else:
        print("DEFEAT")
