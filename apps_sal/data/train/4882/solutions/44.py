def round_to_next5(n):
    if n % 5 == 0:
        return n
    a = n // 5
    return (a + 1) * 5
