def is_digit(n):
    try:
        return n.isdigit() if int(n) <= 9 else False
    except:
        return False
