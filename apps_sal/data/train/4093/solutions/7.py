def find_a(array, n):
    if 0 <= n < 4:
        return array[n]
    a = {i: x for (i, x) in enumerate(array)}
    if n > 4:
        for i in range(4, n + 1):
            a[i] = -a[i - 4] + 6 * a[i - 3] - 10 * a[i - 2] + 6 * a[i - 1]
    else:
        for i in range(-1, n - 1, -1):
            a[i] = 6 * a[i + 1] - 10 * a[i + 2] + 6 * a[i + 3] - a[i + 4]
    return a[i]
