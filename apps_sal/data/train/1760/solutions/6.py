def count(chessBoard):
    d = {}
    count = 0
    size = 2
    l = len(chessBoard)
    coords = []
    for i in range(l):
        for j in range(l):
            if chessBoard[i][j] == 0:
                coords.append([i, j])

    while True:
        for point in coords:
            for i in range(point[0] - size + 1, point[0] + 1):
                chessBoard[i][point[1] - size + 1] = 0
            for i in range(point[1] - size + 1, point[1] + 1):
                chessBoard[point[0] - size + 1][i] = 0

        for i in range(l):
            chessBoard[i][l - size + 1] = 0
        chessBoard[l - size + 1] = [0] * l

        count = sum([sum(x) for x in chessBoard])

        if count > 0:
            d[size] = count
        else:
            break
        size += 1
        count = 0
    return d
