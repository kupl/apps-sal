def is_square(n):
    if n >= 0:
        if int(n ** 0.5) ** 2 == n:
            return True
    return False
