def is_digit(n):
    if len(n) != 1:
        return False
    try:
        if int(n) > -1 and int(n) < 10:
            return True
    except:
        return False
