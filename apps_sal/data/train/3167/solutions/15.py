def twos_difference(a):
    return sorted([(i, j) for i in a for j in a if i - j == -2])
