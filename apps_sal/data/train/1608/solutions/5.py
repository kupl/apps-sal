def sub_determinant(matrix, i):
    sub_matrix = []
    for j in range(1, len(matrix)):
        sub_matrix.append(matrix[j][:i] + matrix[j][i + 1:])
    return sub_matrix


def determinant(matrix):
    if len(matrix) == 0:
        return 0
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        sum = 0
        for i in range(0, len(matrix)):
            if 1 == i & 1:
                sum = sum - matrix[0][i] * determinant(sub_determinant(matrix, i))
            else:
                sum = sum + matrix[0][i] * determinant(sub_determinant(matrix, i))
        return sum
