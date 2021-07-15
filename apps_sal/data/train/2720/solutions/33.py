def n(digits):
    digits = str(digits)
    k = []
    i = 0
    while i<len(digits):
        k += [int(digits[i:i+5])]
        i += 1
    return k
            

solution = lambda digits: max(n(digits))
