def pack_bagpack(val, w, t):
    if sum(w) <= t : return sum(val)
    matrix = [[0 for _ in range(t + 1)] for _ in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, t + 1):
            matrix[i][j] = matrix[i-1][j] if j<w[i-1] else max(matrix[i-1][j],val[i-1]+matrix[i-1][j-w[i-1]])
    return matrix[-1][-1]
