def series_slices(digits, n):
    if n > len(digits):
        0 / 0
    return [list(map(int, digits[x:n+x])) for x in range((len(digits) - n) + 1)]
