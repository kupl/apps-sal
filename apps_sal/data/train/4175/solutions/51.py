def repeater(string, n):
    str = ''
    while n > 0:
        str = str + string
        n = n - 1
    return str
