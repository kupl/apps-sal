t = int(input())
for i in range(t):
    (n, m, x, y) = list(map(int, input().split()))
    n1 = n - 1
    m1 = m - 1
    if n1 % x == 0 and m1 % y == 0:
        print('Chefirnemo')
    elif (n1 - 1) % x == 0 and (m1 - 1) % y == 0 and (n1 > 0) and (m1 > 0):
        print('Chefirnemo')
    else:
        print('Pofik')
