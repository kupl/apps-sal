from numpy import matrix


def get_matrix_product(a, b):
    m1, m2 = matrix(a), matrix(b)
    return (m1 * m2).tolist() if m1.shape[1] == m2.shape[0] else -1


getMatrixProduct = get_matrix_product
