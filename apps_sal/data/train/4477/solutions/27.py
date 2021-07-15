def reverse_number(n):
    sN = str(n)
    x = sN[::-1]
    new = ''
    for i in x:
        if i =='-':
            continue
        else:
            new+=i
    if n < 0:
        return -int(new)
    else:
        return int(new)
