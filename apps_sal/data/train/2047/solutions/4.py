def __starting_point():
    numbers = list(map(int, input().split()))
    n = numbers[0]
    k = numbers[1]
    left = 0
    left = k
    table = []
    x = 4
    while x > 0:
        table.append(list(map(int, input().split())))
        x = x - 1
    moves = []
    for i in range(n):
        if table[1][i] == table[0][i] and table[1][i] != 0:
            moves.append((table[1][i], 1, i + 1))
            table[0][i] = table[1][i]
            table[1][i] = 0
        if table[2][i] == table[3][i] and table[2][i] != 0:
            moves.append((table[2][i], 4, i + 1))
            table[3][i] = table[2][i]
            table[2][i] = 0
    ok = 0
    for i in range(n):
        if table[1][i] == 0:
            ok = 1
            break
        if table[2][i] == 0:
            ok = 1
            break
    if ok == 0:
        print(-1)
        return
    for i in range(20000):
        if table[1][0] != 0 and table[2][0] == 0:
            moves.append((table[1][0], 3, 1))
            table[2][0] = table[1][0]
            table[1][0] = 0
            if n == 1:
                continue
        for j in range(1, n):
            if table[1][j - 1] == 0 and table[1][j] != 0:
                moves.append((table[1][j], 2, j))
                table[1][j - 1] = table[1][j]
                table[1][j] = 0
        for j in range(n):
            if table[1][j] == table[0][j] and table[1][j] != 0:
                moves.append((table[1][j], 1, j + 1))
                table[0][j] = table[1][j]
                table[1][j] = 0
            if table[2][j] == table[3][j] and table[2][j] != 0:
                moves.append((table[2][j], 4, j + 1))
                table[3][j] = table[2][j]
                table[2][j] = 0
        if table[1][n - 1] == 0 and table[2][n - 1] != 0:
            moves.append((table[2][n - 1], 2, n))
            table[1][n - 1] = table[2][n - 1]
            table[2][n - 1] = 0
        for j in range(n - 2, -1, -1):
            if table[2][j + 1] == 0 and table[2][j] != 0:
                moves.append((table[2][j], 3, j + 2))
                table[2][j + 1] = table[2][j]
                table[2][j] = 0

        for j in range(n):
            if table[1][j] == table[0][j] and table[1][j] != 0:
                moves.append((table[1][j], 1, j + 1))
                table[0][j] = table[1][j]
                table[1][j] = 0
            if table[2][j] == table[3][j] and table[2][j] != 0:
                moves.append((table[2][j], 4, j + 1))
                table[3][j] = table[2][j]
                table[2][j] = 0
    if len(moves) > 20000:
        print(-1)
        return
    print(len(moves))
    for j in moves:
        print(*j)


__starting_point()
