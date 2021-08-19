def is_digit(n):
    if len(n) == 1:
        try:
            x = int(n)
            return True if x < 10 and x >= 0 else False
        except:
            return False
    else:
        return False
