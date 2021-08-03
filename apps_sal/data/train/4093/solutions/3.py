def find_a(array, n):
    if 0 <= n < 4:
        return array[n]
    b1 = 3 * array[1] - array[0] - array[2]
    b2 = 3 * array[2] - array[1] - array[3]
    b3 = 3 * b2 - b1 - array[2]
    b0 = 3 * b1 - b2 - array[1]
    array_b = [b0, b1, b2, b3]

    if n > 3:
        count = 3
    else:
        array.reverse()
        array_b.reverse()
        count = 0
        n = 0 - n
    while count < n:
        a_next = 3 * array[-1] - array[-2] - array_b[-1]
        b_next = 3 * array_b[-1] - array_b[-2] - array[-1]
        array.append(a_next)
        array_b.append(b_next)
        count += 1

    return array[-1]
