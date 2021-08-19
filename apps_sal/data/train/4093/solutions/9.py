def find_a(array, n):
    if 0 <= n <= 3:
        return array[n]
    a0 = array[0]
    a1 = array[1]
    a2 = array[2]
    a3 = array[3]
    b1 = 3 * a1 - a0 - a2
    b2 = 3 * a2 - a1 - a3
    b3 = 3 * b2 - b1 - a2
    b0 = 3 * b1 - b2 - a1
    if n > 3:
        for k in range(4, n + 1, 1):
            an = 3 * a3 - a2 - b3
            bn = 3 * b3 - b2 - a3
            (a2, a3) = (a3, an)
            (b2, b3) = (b3, bn)
    else:
        for k in range(-1, n - 1, -1):
            an = 3 * a0 - a1 - b0
            bn = 3 * b0 - b1 - a0
            (a0, a1) = (an, a0)
            (b0, b1) = (bn, b0)
    return an
