def get_candy_position(n, row, column, element):
    (arr, arr_p, row_p, col_p) = ([[[0] * column for i in range(row)]], 0, row - 1, column - 1)
    i = 1
    while i < n + 1:
        arr[arr_p][row_p][col_p] = i
        col_p -= 1
        if col_p < 0:
            col_p = column - 1
            row_p -= 1
        if all([k != 0 for j in arr for k in sum(j, [])]):
            arr.append([[0] * column for i in range(row)])
            row_p = row - 1
            arr_p += 1
        i += 1
    final = [[i + 1, j, y.index(element)] for (i, x) in enumerate(arr) for (j, y) in enumerate(x) if element in y]
    return final[0] if final else [-1, -1, -1]
