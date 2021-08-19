def min_value(digits):
    return int(''.join(sorted({str(m) for m in digits})))
