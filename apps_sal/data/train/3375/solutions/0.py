def going(n):
    s = 1.0
    for i in range(2, n + 1):
        s = s / i + 1
    return int(s * 1000000.0) / 1000000.0
