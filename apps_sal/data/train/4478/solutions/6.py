def sum_to_infinity(A):
    r = A[1] / A[0]
    if abs(r) >= 1:
        return "No Solutions"
    else:
        return round(A[0] / (1 - r), 3)
