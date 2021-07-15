def series_slices(digits, n):
    digits = [int(i) for i in digits]
    if n > len(digits):
         raise Error('Your n is bigger than the lenght of digits')        
    else:
        return [list(digits[i:n+i]) for i in range(len(digits)) if len(digits[i:n+i]) == n]
