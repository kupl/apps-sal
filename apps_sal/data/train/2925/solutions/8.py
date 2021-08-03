def multiply(n):
    nDigits = len(str(abs(n)))
    print(nDigits)
    return n * (5**nDigits)
