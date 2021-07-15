def going(n):
    factor = 1.0
    acc = 1.0
    for i in range(n, 1, -1):
        factor *= 1.0 / i
        acc += factor
    return int(acc * 1e6) / 1e6
