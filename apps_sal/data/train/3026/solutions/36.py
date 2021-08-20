def min_value(digits):
    d = ''.join([str(i) for i in sorted(list(set(digits)))])
    return int(d)
