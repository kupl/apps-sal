def add_binary(a,b):
    s = a+b
    fin = []
    while s != 0:
        quo  = s//2
        rem = s%2
        fin.append(rem)
        s = quo
    fin.reverse()
    return ''.join(map(str,fin))
