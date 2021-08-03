def matrix_addition(A, B):
    return [[cellA + cellB for cellA, cellB in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
