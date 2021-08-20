t = int(input())
for c in range(t):
    (x, y) = list(map(int, input().split()))
    f = 0
    while x != 1 and y != 1 and (f == 0):
        if y > x and y % x == 0:
            f = 1
        elif y > x:
            y = y % x
        elif x > y and x % y == 0:
            f = 1
        elif x > y:
            x = x % y
        elif x == y and x != 1:
            f = 1
    if f == 0:
        print('YES')
    else:
        print('NO')
