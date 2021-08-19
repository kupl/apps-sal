def arithmetic_sequence_sum(a, r, n):
    return sum((a + sum((r for _ in range(i))) for i in range(n)))
