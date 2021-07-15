def series_slices(digits, n):
    if n > len(digits):
        raise ValueError
    else:
        return [[int(digit) for digit in digits[i:i+n]] for i in range(0, len(digits)-n+1)]
