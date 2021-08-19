def repeater(string, n):
    a = 0
    b = ''
    while a < n:
        b = b + string
        a += 1
    return b
