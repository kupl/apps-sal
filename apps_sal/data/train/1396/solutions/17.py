t = int(input())
while t > 0:
    t -= 1
    (n, m, x, y) = [int(x) for x in input().split()]
    f = 0
    if m == 1 and n == 1:
        f = 1
    elif n == 2 and m == 2:
        f = 1
    elif (n - 1) % x == 0 and (m - 1) % y == 0 and (n >= 1) and (m >= 1):
        f = 1
    elif n >= 2 and m >= 2:
        if (n - 2) % x == 0 and (m - 2) % y == 0:
            f = 1
    if f == 1:
        print('Chefirnemo')
    else:
        print('Pofik')
