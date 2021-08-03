def min_value(digits):
    return int(''.join(map(str, (sorted(set(map(int, digits)))))))
