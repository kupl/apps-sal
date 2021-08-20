for _ in range(int(input())):
    (v1, t1, v2, t2, v3, t3) = map(int, input().split())
    x = t2 - t3
    y = t3 - t1
    if t1 <= t3 <= t2:
        if x * v3 <= (x + y) * v1 and y * v3 <= (x + y) * v2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
