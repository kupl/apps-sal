import math
t = int(input())
for q in range(t):
    (n, m, x, y) = map(int, input().split(' '))
    if n == 1 and m == 1:
        print('Chefirnemo')
    elif n == 2 and m == 2:
        print('Chefirnemo')
    elif x == 1 and n != 1 and ((m - 1) % y == 1):
        print('Chefirnemo')
    elif y == 1 and m != 1 and ((n - 1) % x == 1):
        print('Chefirnemo')
    elif x == 1 and y == 1:
        print('Chefirnemo')
    elif x == 0 and y == 0:
        print('Pofik')
    elif (n - 1) % x == 0 and (m - 1) % y == 0:
        print('Chefirnemo')
    elif (n - 1) % x == 1 and (m - 1) % y == 1:
        print('Chefirnemo')
    else:
        print('Pofik')
