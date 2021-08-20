t = int(input())
for _ in range(t):
    (n, m, x, y) = [int(x) for x in input().split()]
    n -= 1
    m -= 1
    if n == 0 and m == 0 or (n == 1 and m == 1):
        print('Chefirnemo')
        continue
    if n % x == 0 and m % y == 0:
        print('Chefirnemo')
        continue
    f = 0
    if n > 0 and m > 0:
        if n % x == 1 and m % y == 1:
            f = 1
            print('Chefirnemo')
        elif x == 1 and m % y in [0, 1]:
            f = 1
            print('Chefirnemo')
        elif y == 1 and n % x in [0, 1]:
            f = 1
            print('Chefirnemo')
    if f == 0:
        print('Pofik')
