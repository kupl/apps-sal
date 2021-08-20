def twos_difference(A):
    L = []
    for i in sorted(A):
        if i + 2 in A:
            L.append((i, i + 2))
    return L
