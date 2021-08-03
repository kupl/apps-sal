def poly_multiply(p1, p2):
    result = [0 for _ in range(len(p1) + len(p2) - 1)]
    for i, n1 in enumerate(p1):
        for j, n2 in enumerate(p2):
            result[i + j] += n1 * n2
    return [] if not p1 or not p2 else result
