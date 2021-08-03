def powers_of_two(n):
    result = []
    a = 0
    while a < n + 1:
        b = 2**a
        result.append(b)
        a = a + 1
    return result
