def levenshtein(a, b):
    import numpy as np
    size_x = len(a) + 1
    size_y = len(b) + 1
    matrix = np.empty((size_x, size_y))
    matrix[:, 0] = list(range(size_x))
    matrix[0, :] = list(range(size_y))

    for x in range(1, size_x):
        for y in range(1, size_y):
            if a[x - 1] == b[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
    return (int(matrix.item((size_x - 1, size_y - 1))))
