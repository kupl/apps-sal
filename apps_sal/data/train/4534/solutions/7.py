def find_next_power(val, pow_):
    return round((int(val ** (1.0 / pow_)) + 1) ** pow_)
