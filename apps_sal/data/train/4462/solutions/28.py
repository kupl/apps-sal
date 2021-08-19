def adjacent_element_product(A):
    return max([a * b for (a, b) in zip(A[:-1], A[1:])])
