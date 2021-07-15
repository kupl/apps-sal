def min_value(digits):
    unique_sorted_d = sorted(set(digits))
    return int(''.join(map(str, unique_sorted_d)))
