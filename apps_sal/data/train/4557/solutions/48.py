def row_weights(A):
    return (sum((e for (i, e) in enumerate(A) if not i % 2)), sum((e for (i, e) in enumerate(A) if i % 2)))
