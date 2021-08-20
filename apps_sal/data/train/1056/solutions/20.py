for i in range(int(input())):
    (b, t, s) = map(int, input().split())
    if b + t + s == 180:
        print('YES')
    else:
        print('NO')
