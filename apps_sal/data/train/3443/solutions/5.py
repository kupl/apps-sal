def correct(m, n, bits):

    def invert(n):
        if n == 1:
            return 0
        if n == 0:
            return 1
        else:
            return None
    matrix = []
    wrong_row = None
    wrong_col = None
    n_list = [int(x) for x in bits[m * n + m:]]
    m_list = [int(x) for x in bits[m * n:m * n + m]]
    for i in range(m):
        row = [int(x) for x in bits[n * i:n * i + n]]
        if sum(row) % 2 != m_list[i]:
            wrong_row = i
        matrix.append(row)
    col = []
    for j in range(n):
        for i in range(m):
            col.append(matrix[i][j])
        if sum(col) % 2 != n_list[j]:
            wrong_col = j
        col = []
    if wrong_col == None and wrong_row != None:
        m_list[wrong_row] = invert(m_list[wrong_row])
    elif wrong_col != None and wrong_row == None:
        n_list[wrong_col] = invert(n_list[wrong_col])
    elif wrong_col != None and wrong_row != None:
        matrix[wrong_row][wrong_col] = invert(matrix[wrong_row][wrong_col])
    res = ''
    for matrix_row in matrix:
        res += ''.join([str(x) for x in matrix_row])
    res += ''.join([str(x) for x in m_list])
    res += ''.join([str(x) for x in n_list])
    return res
