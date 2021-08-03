def descriptions(arr):
    r, prev, n = 1, arr[0], 1
    for x in arr[1:]:
        if x != prev + 1:
            r *= 2 ** (n - 1)
            n = 0
        prev = x
        n += 1
    return r * 2 ** (n - 1)
