def get_matrix(n):
    # your code here
    matrix = []

    for idx in range(0, n):
        child_matrix = []
        child_matrix += ([0] * idx) + [1] + ([0] * (n - 1 - idx))
        matrix.append(child_matrix)
    return matrix
