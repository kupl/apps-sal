def series_slices(digits, n):
    if n > len(digits):
        raise error
    else:
        x = [int(y) for y in digits]
        return [x[i:i+n] for i in range(0,len(digits)-n+1)]
