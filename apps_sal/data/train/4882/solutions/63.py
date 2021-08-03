def round_to_next5(n):
    remainder = n % 5

    if remainder == 0:
        return n

    if remainder > 0:
        missing_value = 5 - remainder
        return n + missing_value
