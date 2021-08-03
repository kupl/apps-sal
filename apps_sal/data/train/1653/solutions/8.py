def fibfusc(n, num_digits=None):
    arr = []
    (x, y) = (0, 1)

    if num_digits:
        MOD = 10**num_digits
    if n == 0:
        return (1, 0)

    while n > 1:
        arr.append(n)
        n //= 2
    arr = list(reversed(arr))

    for i in arr:
        if i % 2 == 0:
            (x, y) = (((x + y) * (x - y), y * (2 * x + 3 * y)))
        else:
            (x, y) = ((-y * (2 * x + 3 * y), (x + 2 * y) * (x + 4 * y)))
        if num_digits:
            (x, y) = (x % MOD, y % MOD)

    if arr and num_digits:
        x = -MOD + (x % MOD)
    return (x, y)
