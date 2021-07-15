def multiply(n):
    return n*pow(5, len(str(n))-1) if n < 0 else n*pow(5, len(str(n)))
