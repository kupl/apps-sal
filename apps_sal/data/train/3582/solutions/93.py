def is_digit(n):
    if len(n) > 1:
        return False
    try:
        int(n)
        return True
    except:
        return False
