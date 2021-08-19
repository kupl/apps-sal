for _ in range(int(input())):
    mat = []
    (n, m) = map(int, input().split())
    for i in range(n):
        mat.append(list(input()))
    d = [0] * (n + m)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '1':
                for x in range(n):
                    for y in range(m):
                        if mat[x][y] == '1':
                            d[abs(x - i) + abs(y - j)] += 1
    for i in range(1, n + m - 1):
        print(d[i] // 2, end=' ')
