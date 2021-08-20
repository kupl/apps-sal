def add_binary(a, b):
    x = a + b
    newstr = ''
    while x > 0:
        bin = x % 2
        newstr += str(bin)
        x = x // 2
    newstr = newstr[::-1]
    return newstr
