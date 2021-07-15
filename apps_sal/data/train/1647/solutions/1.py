def next_bigger(n):
    # algorithm: go backwards through the digits
    # when we find one that's lower than any of those behind it,
    # replace it with the lowest digit behind that's still higher than it
    # sort the remaining ones ascending and add them to the end
    digits = list(str(n))
    for pos, d in reversed(tuple(enumerate(digits))):
        right_side = digits[pos:]
        if d < max(right_side):
            # find lowest digit to the right that's still higher than d
            first_d, first_pos = min((v, p) for p, v in enumerate(right_side) if v > d)

            del right_side[first_pos]
            digits[pos:] = [first_d] + sorted(right_side)

            return int(''.join(digits))

    return -1

