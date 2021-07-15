def is_digit(n):
    if n.isdigit() and n!='' and int(n) < 10:
        return True
    else:
        return False
