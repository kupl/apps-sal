def arithmetic_sequence_elements(a, r, n):
    result = [str(a)]
    for i in range(1, n):
        a = a + r
        result.append(str(a))
    return ', '.join(result)
