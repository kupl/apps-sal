def five_by_2n(n):
    b = [8, 95, 1183, 14824]
    if n <= 4:
        return b[n - 1]
    for i in range(4,n):
        b.append((15*b[i-1] - 32*b[i-2] + 15*b[i-3] - b[i-4])%12345787)
    return b[-1]

