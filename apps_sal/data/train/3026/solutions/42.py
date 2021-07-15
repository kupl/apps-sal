def min_value(digits):
    unique_digits = set(digits)
    min_number = 0
    for integer in sorted(unique_digits):
        min_number *= 10
        min_number += integer
    return min_number

