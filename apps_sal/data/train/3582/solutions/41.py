def is_digit(n):
    s = "0123456789"
    if n in s and len(n) == 1:
        return True
    else:
        return False
