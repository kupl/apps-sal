def is_digit(n):
    if len(n) == 1:
        try:
            if int(n) < 10:
                return isinstance(int(n), int)
            return False
        except ValueError:
            return False
    return False
