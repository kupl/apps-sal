def isDigit(s):
    if s.isalnum():
        return False
    k = s.isnumeric() or is_number(s)
    return k


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
