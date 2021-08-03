def arithmetic_sequence_elements(a, r, n):
    def seq(a, r, n):
        while n > 0:
            yield a
            n -= 1
            a += r
    return ", ".join(map(str, seq(a, r, n)))
