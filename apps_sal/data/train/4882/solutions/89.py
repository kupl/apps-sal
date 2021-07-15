def round_to_next5(n):
    a = n % 5
    if a == 0:
        return n
    if a == 1:
        return n + 4
    if a == 2:
        return n + 3
    if a == 3:
        return n + 2
    if a == 4:
        return n + 1
