def matrix_addition(a, b):
    return [[sum(xs) for xs in zip(ra, rb)] for ra, rb in zip(a, b)]
