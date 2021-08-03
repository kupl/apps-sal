def two_sort(array):
    x = sorted(array)
    y = x[0]
    return '***'.join(y[i:i + 1] for i in range(0, len(y)))
