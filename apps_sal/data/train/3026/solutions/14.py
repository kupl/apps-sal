def min_value(digits):
    return int(''.join(sorted(set((str(x) for x in digits)))))
