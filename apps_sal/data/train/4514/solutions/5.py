def int_to_negabinary(i):
    if not i:
        return '0'
    digits = []
    while i != 0:
        (i, r) = divmod(i, -2)
        (i, r) = (i + 1, r + 2) if r < 0 else (i, r)
        digits.append(str(r))
    return ''.join(digits[::-1])


def negabinary_to_int(s):
    return sum([int(c) * (-2) ** i for (i, c) in enumerate(s[::-1])])
