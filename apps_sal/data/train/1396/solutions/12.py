for _ in range(int(input())):
    (n, m, x, y) = list(map(int, input().split()))
    n = n - 1
    m = m - 1
    flag = 0
    if n % x == 0 and flag == 0:
        if m % y == 0 and flag == 0:
            print('Chefirnemo')
            flag = 1
    if n > 0 and m > 0:
        if (n - 1) % x == 0 and (m - 1) % y == 0 and (flag == 0):
            print('Chefirnemo')
            flag = 1
    if flag == 0:
        print('Pofik')
