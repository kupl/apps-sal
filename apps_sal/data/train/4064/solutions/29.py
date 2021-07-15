def count_by(x, n):
    y = []
    ind = 1
    for i in range(n):
        y.append((x * ind))
        ind += 1
    return y
