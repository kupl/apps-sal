def reverse_number(n):
    a = str(n)[::-1]
    b = ''
    if '-' in a:
        b = '-' + a[:-1]
        return int(b)
    else:
        return int(a) 
