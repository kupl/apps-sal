n = int(input())
for j in range(n):
    p = input().split(' ')
    a = int(p[0])
    k = int(p[1])
    x = input().split(' ')
    x1 = int(x[0])
    x2 = int(x[1])
    x3 = int(x[2])
    x = min(x1, x2, x3)
    y = max(x1, x2, x3)
    area = 0
    if y - x - 2 * k >= a:
        area = 0
    elif y - x <= 2 * k:
        area = a * a
    else:
        area = (a - (y - x - 2 * k)) * a
    print('{0:.2f}'.format(area))
