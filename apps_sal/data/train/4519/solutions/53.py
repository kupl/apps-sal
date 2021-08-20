def max_number(n):
    s = ''
    a = sorted((int(i) for i in str(n)))[::-1]
    for j in a:
        s += str(j)
    return int(s)
