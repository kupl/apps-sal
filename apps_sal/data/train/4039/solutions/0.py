def transform(num, base):
    digits = []
    while num > 0:
        (num, remainder) = divmod(num, base)
        digits.append(remainder if remainder < 10 else 'x')
    return digits


def fouriest(i):
    (max_fours, base, best) = (0, 5, [None, None])
    while i >= base ** max_fours:
        digits = transform(i, base)
        if digits.count(4) > max_fours:
            max_fours = digits.count(4)
            best = (base, ''.join(map(str, digits[::-1])))
        base += 1
    (base, transformed) = best
    return '%s is the fouriest (%s) in base %s' % (i, transformed, base)
