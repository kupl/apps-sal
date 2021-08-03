def round_to_next5(n):
    for item in range(n, n + 5):
        if item % 5 == 0:
            return item
