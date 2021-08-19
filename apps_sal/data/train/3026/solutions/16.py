def min_value(digits):
    # your code here
    return int(''.join(sorted({str(m) for m in digits})))
