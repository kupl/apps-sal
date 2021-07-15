def min_value(digits):
    digits = set(digits)
    ord = sorted(digits)
    new = ""
    for i in ord:
        new += str(i)
    return int(new)
