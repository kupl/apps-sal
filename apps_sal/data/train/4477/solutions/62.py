def reverse_number(n):
    res = []
    s = str(n)
    if s[0] == '-':
        res = "-" + s[:0:-1]
    else:
        res = s[::-1]
    return int(res)
