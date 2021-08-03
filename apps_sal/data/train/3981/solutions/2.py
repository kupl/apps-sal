def arithmetic_sequence_sum(a, r, n):
    result = 0
    for i in range(n):
        result += a + i * r
    return result
