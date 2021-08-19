def is_very_even_number(n):
    return True if not n else all((not n % 9 % 2, n % 9))
