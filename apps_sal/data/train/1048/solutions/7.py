t = int(input())
for o in range(t):
    n, k = list(map(int, input().split()))
    x, y, z = list(map(int, input().split()))
    x1, y1 = x - n / 2, x + n / 2
    x2, y2 = y - n / 2, y + n / 2
    x3, y3 = z - n / 2, z + n / 2
    a = [(x1 - k, y1 + k), (x2 - k, y2 + k), (x3 - k, y3 + k)]
    a.sort()
    x1, y1 = a[0]
    x2, y2 = a[1]
    x3, y3 = a[2]
    f1, f2 = max(x1, x2), min(y1, y2)
    ans = 0.0
    flag = False
    if(f1 >= f2):
        flag = True
    else:
        f1 = max(f1, x3)
        f2 = min(f2, y3)
        if(f1 >= f2):
            flag = True
    if(flag):
        print(0 * 1.0)
        continue
    if(f2 - f1 > n):
        print(n * n * 1.0)
    else:
        print((f2 - f1) * n * 1.0)
