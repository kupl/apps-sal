def calc_type(a, b, res):
    if a + b == res:
        return 'addition'
    if a - b == res:
        return 'subtraction'
    return 'multiplication' if a * b == res else 'division'
