def round_to_next5(n):
    a = (n // 5) * 5
    b = a + 5
    if a == n:
        return n
    elif a > b:
        return a
    else:
        return b
