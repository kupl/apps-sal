def crossing_sum(a, b, c):
    return sum(a[b]) + sum(x[c] for x in a) - a[b][c]
