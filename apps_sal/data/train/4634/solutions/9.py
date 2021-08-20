def pac_man(N, PM, enemies):
    print(N)
    print(PM)
    print(enemies)
    board = []
    row = []
    column = []
    if enemies == []:
        return N ** 2 - 1
    for i in enemies:
        row.append(PM[1] - i[1])
        column.append(PM[0] - i[0])
    rowMinus = [(PM[1] - N) * -1]
    rowPlus = [PM[1] + 1]
    columnMinus = [(PM[0] - N) * -1]
    columnPlus = [PM[0] + 1]
    for i in row:
        if i < 0:
            rowMinus.append(i * -1)
        else:
            rowPlus.append(i)
    for i in column:
        if i < 0:
            columnMinus.append(i * -1)
        else:
            columnPlus.append(i)
    ColumnD = min(rowPlus) + min(rowMinus) - 1
    RowD = min(columnPlus) + min(columnMinus) - 1
    print('x')
    (print(RowD), print(columnPlus), print(columnMinus))
    print(ColumnD)
    return ColumnD * RowD - 1
