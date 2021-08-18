def round_to_next5(n):
    rem = n % 5
    return n + ((5 - rem) if rem else 0)
