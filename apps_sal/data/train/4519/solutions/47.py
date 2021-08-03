def max_number(n):
    a = []
    s = ''
    for i in str(n):
        a.append(int(i))
    b = sorted(a, reverse=True)
    for j in b:
        s += str(j)
    return int(s)
