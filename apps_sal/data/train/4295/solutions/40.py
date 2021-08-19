def balanced_num(n):
    (n, sr, sl) = (str(n), 0, 0)
    while len(n) > 2:
        sl += int(n[0])
        sr += int(n[-1])
        n = n[1:-1]
    return 'Balanced' if sr == sl else 'Not Balanced'
