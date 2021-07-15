def add_binary(a,b):
    r = a + b
    s = ''
    while (r > 0):
        s += '1' if r % 2 == 1 else '0'
        r = r >> 1
    
    return s[::-1]
