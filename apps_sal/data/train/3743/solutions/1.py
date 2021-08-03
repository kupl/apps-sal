def chess_board(rows, columns):
    ans = []
    for i in range(1, rows + 1, 1):
        l = []
        for j in range(i, columns + i, 1):
            if j % 2 != 0:
                l.append('O')
            else:
                l.append('X')
        ans.append(l)
    return ans
