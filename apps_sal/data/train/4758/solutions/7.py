def connect_four_place(columns):
    mat = [[] for _ in range(7)]
    ply = 0
    for col in columns:
        mat[col].append('YR'[ply])
        ply ^= 1
    for col in mat:
        while len(col) < 6: col.append('-')
    return [list(row) for row in zip(*mat)][::-1]
