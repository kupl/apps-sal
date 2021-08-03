def is_divide_by(number, a, b):
    if divmod(number, a)[1] == divmod(number, b)[1] == 0:
        return True
    return False
