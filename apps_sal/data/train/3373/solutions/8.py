def matrix_mult(A, B):

    def item_multiply(x, y):
        return sum((x[i] * y[i] for i in range(len(x))))
    B = [[j[i] for j in B] for i in range(len(B[0]))]
    result = []
    cycles = list(range(len(A)))
    for k in cycles:
        items = []
        for l in cycles:
            items.append(item_multiply(A[k], B[l]))
        result.append(items)
    return result
