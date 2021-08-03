def matrix_mult(A, B):
    # Multiply two lists index by index
    def item_multiply(x, y): return sum(x[i] * y[i] for i in range(len(x)))
    # Reverse the matrix to allow index by index multiplication
    B = [[j[i] for j in B] for i in range(len(B[0]))]
    result = []
    # Go line by line on matrix a
    cycles = list(range(len(A)))
    for k in cycles:
        items = []
        # Add all lists multiplications to a list
        for l in cycles:
            items.append(item_multiply(A[k], B[l]))
        # Then add these multiplications list to the result
        result.append(items)
    return result
