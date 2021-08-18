T = int(input())
for i in range(0, T):
    a = 0
    b = 0
    N, K, x, y = map(int, input().split())
    if x == y:
        a = N
        b = N
    elif x > y:
        if K % 4 == 1:
            a = N
            b = y - x + N
        elif K % 4 == 2:
            a = y - x + N
            b = N
        elif K % 4 == 3:
            a = 0
            b = x - y
        else:
            a = x - y
            b = 0
    else:
        if K % 4 == 1:
            a = x - y + N
            b = N
        elif K % 4 == 2:
            a = N
            b = x - y + N
        elif K % 4 == 3:
            a = y - x
            b = 0
        else:
            a = 0
            b = y - x
    print(a, b)
