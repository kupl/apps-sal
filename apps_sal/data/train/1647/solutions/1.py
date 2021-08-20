def next_bigger(n):
    digits = list(str(n))
    for (pos, d) in reversed(tuple(enumerate(digits))):
        right_side = digits[pos:]
        if d < max(right_side):
            (first_d, first_pos) = min(((v, p) for (p, v) in enumerate(right_side) if v > d))
            del right_side[first_pos]
            digits[pos:] = [first_d] + sorted(right_side)
            return int(''.join(digits))
    return -1
