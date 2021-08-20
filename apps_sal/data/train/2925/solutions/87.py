def multiply(n):
    digits = len(list(str(n).lstrip('-')))
    return n * 5 ** digits
