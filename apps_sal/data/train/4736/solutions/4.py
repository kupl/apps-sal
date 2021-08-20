def how_many_bees(hive):
    if not hive:
        return 0

    def row_bees(row):
        return sum((1 for i in range(len(row)) if ''.join(row[i:i + 3]) == 'bee'))

    def matrix_bees(matrix):
        return sum((row_bees(row) for row in matrix))

    def v_flip(matrix):
        return [row[::-1] for row in matrix]

    def transpose(matrix):
        return [list(z) for z in zip(*matrix)]
    return matrix_bees(hive) + matrix_bees(transpose(hive)) + matrix_bees(v_flip(hive)) + matrix_bees(v_flip(transpose(hive)))
