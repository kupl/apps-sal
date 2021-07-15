def find_difference(a, b):
    A = B = 1
    for i, j in zip(a, b):
        A *= i
        B *= j
    return abs(A - B)
