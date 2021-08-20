def round_to_next5(n):
    if n == 0 or abs(n) % 5 == 0:
        return n
    else:
        for i in range(6):
            if (n + i) % 5 == 0:
                return n + i
