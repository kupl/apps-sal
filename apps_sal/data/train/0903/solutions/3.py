t = int(input())
while t > 0:
    (x1, y1) = input().split()
    (x2, y2) = input().split()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    x = min(x1, x2)
    if x == x1:
        ans = y1 * (x2 - x1) / (y1 + y2)
        ans = x1 + ans
    else:
        ans = y2 * (x1 - x2) / (y1 + y2)
        ans = x2 + ans
    print('%.2f' % ans)
    t = t - 1
