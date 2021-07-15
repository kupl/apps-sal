def multiply(n):
    x = len(str(n).lstrip('-').replace('.',''))
    return n * (5**x)

