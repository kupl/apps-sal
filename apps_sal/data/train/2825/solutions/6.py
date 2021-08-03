def even_magic(n):
    square = []
    for j in range(0, n):
        row = []
        for i in range(0, n):
            v = i + j * n + 1
            if i % 4 == j % 4 or -(i + 1) % 4 == j % 4:
                row.append(n**2 + 1 - v)
            else:
                row.append(v)
        square.append(row)
    return square
