def series_slices(digits, n):
    assert n <= len(digits)
    return [list(map(int, digits[i: i+n])) for i in range(len(digits)-n+1)]
