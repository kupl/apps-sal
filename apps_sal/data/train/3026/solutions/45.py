def min_value(digits):
    s = set()
    for x in digits:
        for d in str(x):
            s.add(d)
    return int(''.join(sorted(s)))
