def series_slices(digits, n):
    if n > len(digits):
        raise ValueError('n cannot be greater than number of digits')
    
    else:
        res = [digits[i:i+n] for i in range(len(digits) - n + 1)]
        for i in range(len(res)):
            res[i] = [int(e) for e in res[i]]

        return res
