def different_squares(matrix):
    result = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            one = [
                matrix[i][j:j + 2],
                matrix[i + 1][j:j + 2]
            ]
            if one not in result:
                result.append(one)
    return len(result)

