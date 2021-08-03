def multiplication_table(row, col):
    l = []
    for linha in range(row):
        l.append(list(range(linha + 1, (linha + 1) * col + 1, linha + 1)))
    return l
