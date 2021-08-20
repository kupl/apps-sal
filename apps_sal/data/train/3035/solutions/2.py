def getMatrixProduct(a, b):
    if len(a[0]) != len(b):
        return -1
    return [[sum((m * n for (m, n) in zip(a_row, b_col))) for b_col in zip(*b)] for a_row in a]
