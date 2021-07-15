def round_to_next5(n):
    nearest_multiple = 5 * round(n / 5)
    if nearest_multiple < n:
        nearest_multiple = nearest_multiple + 5
    return nearest_multiple
