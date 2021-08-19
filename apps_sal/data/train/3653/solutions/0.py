def tops(msg):
    n = len(msg)
    (res, i, j, k) = ('', 2, 2, 7)
    while i < n:
        res = msg[i:i + j] + res
        (i, j, k) = (i + k, j + 1, k + 4)
    return res
