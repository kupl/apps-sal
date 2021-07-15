def how_many_bees(hive):
    if not hive:
        return 0
    row_bees = lambda row: sum(1 for i in range(len(row)) if "".join(row[i:i+3]) == "bee")
    matrix_bees = lambda matrix: sum(row_bees(row) for row in matrix)
    v_flip = lambda matrix: [row[::-1] for row in matrix]
    transpose = lambda matrix: [list(z) for z in zip(*matrix)]
    return (
        matrix_bees(hive) + 
        matrix_bees(transpose(hive)) +
        matrix_bees(v_flip(hive)) + 
        matrix_bees(v_flip(transpose(hive)))
    )

