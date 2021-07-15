def smallest_integer(matrix):
    i = 0
    matrix = sum(matrix, [])
    while True:
        if i not in matrix:
            return i
        i += 1
