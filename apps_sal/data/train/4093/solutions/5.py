def find_a(array, n):
    if n in range(4):
        return array[n]
    if n < 0:
        return find_a([*reversed(array)], 3 - n)
    a1 = array[1]
    a2 = array[2]
    b1 = 3 * array[1] - array[0] - array[2]
    b2 = 3 * array[2] - array[1] - array[3]
    for _ in range(n - 2):
        a1, b1, a2, b2 = a2, b2, 3 * a2 - a1 - b2, 3 * b2 - b1 - a2
    return a2
