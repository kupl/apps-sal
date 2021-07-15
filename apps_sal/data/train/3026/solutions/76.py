def min_value(digits):
    return int(''.join(sorted([str(digit) for digit in set(digits)])))
