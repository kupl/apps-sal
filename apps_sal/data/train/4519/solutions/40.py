def max_number(n):
    array = list(str(n))
    numb = ''.join(sorted(array, reverse=True))
    s = int(numb)
    return s

