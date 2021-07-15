def round_to_next5(n):
    diff = 5 - (n % 5)
    return n if diff == 5 else n + diff
