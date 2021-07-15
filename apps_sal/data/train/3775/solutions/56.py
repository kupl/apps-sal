def digits(n):
    digits = []
    if n>= 0:
       [digits.append(d) for d in str(n)]
    return len(digits)
    pass
