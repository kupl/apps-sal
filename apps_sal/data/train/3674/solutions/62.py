def add_binary(a,b):
    n = a + b
    s = []
    while n != 0:
        n, b = divmod(n, 2)
        s.insert(0,b)
    return ''.join(map(str,s))
