def arithmetic_sequence_elements(a, r, n):
    z = str(a)
    for i in range(n - 1):
        a = a + r
        z = z + ', ' + str(a)
    return z
