def round_to_next5(n):
    if n % 5 == 0:
        return n

    for i in range(5):
        if (n + i) % 5 == 0:
            return n + i
    return n
