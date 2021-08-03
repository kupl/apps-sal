def determinant(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    li = [[m[j][:i] + m[j][i + 1:] for j in range(1, len(m))] for i in range(len(m))]
    return sum(-m[0][i] * (determinant(j)) if i & 1 else m[0][i] * (determinant(j)) for i, j in enumerate(li))
