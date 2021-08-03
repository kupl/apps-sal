def reverse_on_diagonals(matrix):
    copy = [line[:] for line in matrix]
    for i in range(len(matrix)):
        copy[i][i] = matrix[-1 - i][-1 - i]
        copy[i][-1 - i] = matrix[-1 - i][i]

    return copy
