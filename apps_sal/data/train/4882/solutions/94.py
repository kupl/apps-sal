def round_to_next5(n):
    if n % 5 != 0:
        a = n // 5
        b = (a + 1) * 5
        return b
    else:
        return n
