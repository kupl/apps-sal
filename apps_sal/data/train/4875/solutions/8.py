def is_valid_coordinates(c):
    try:
        return all((-r <= float(s) <= r and 'e' not in s for (s, r) in zip(c.split(','), [90, 180, -1])))
    except ValueError:
        return False
