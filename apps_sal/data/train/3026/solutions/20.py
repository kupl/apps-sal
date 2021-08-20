def min_value(digits):
    return int(''.join(sorted(list(map(str, set(digits))))))
