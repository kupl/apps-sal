t = int(input())
while t > 0:
    n = int(input())
    if n % 2 != 0:
        print('YES')
        k = n // 2
        a = [['0' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            d = 0
            for j in range(i + 1, n):
                a[i][j] = '1'
                d += 1
                if d == k:
                    break
            if d < k:
                for j in range(k - d):
                    a[i][j] = '1'
        for u in range(n):
            for p in range(n):
                print(a[u][p], end='')
            print()
    else:
        print('NO')
    t -= 1
