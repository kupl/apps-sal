for _ in range(int(input())):
    n, m, a, b = list(map(int, input().split()))
    if a * n != b * m:
        print('NO')
    else:
        ar = []
        for i in range(n):
            ar.append([0] * m)
        x, y = 0, a
        for i in range(n):
            if x < y:
                for j in range(x, y):
                    ar[i][j] = 1
            else:
                for j in range(x, m):
                    ar[i][j] = 1
                for j in range(y):
                    ar[i][j] = 1
            x += a
            y += a
            x %= m
            y %= m
        print('YES')
        for i in range(n):
            print(''.join(map(str, ar[i])))
