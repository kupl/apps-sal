def min_value(digits):
    return int(''.join(sorted(set(map(str, digits)), key=int)))
