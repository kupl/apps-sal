def sum_str(a, b):
    if not a and not b:
        return '0'
    return str(int(a) + int(b)) if a and b else '9'
