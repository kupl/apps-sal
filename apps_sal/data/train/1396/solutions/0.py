t = input()
t = int(t)
for _ in range(t):
    (n, m, x, y) = input().split()
    n = int(n)
    m = int(m)
    x = int(x)
    y = int(y)
    n -= 1
    m -= 1
    flag = 0
    if n % x == 0 and m % y == 0:
        flag = 1
    n -= 1
    m -= 1
    if n >= 0 and m >= 0:
        if n % x == 0 and m % y == 0:
            flag = 1
    if flag == 1:
        print('Chefirnemo')
    else:
        print('Pofik')
