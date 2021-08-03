def digits(n):
    a = str(n)
    b = list(a)
    for element in b:
        if element == ',' or element == '.':
            b.remove(element)
        else:
            pass
    return len(b)
