def string_transformer(s):
    x = []
    s = s.split(' ')
    for i in range(1, 2 * len(s) - 1, 2):
        s.insert(i, ' ')
    print(s)
    if '' in s:
        for i in s:
            i.replace('', ' ')
    print(s)
    s.reverse()
    print(s)
    for i in s:
        for j in i:
            if j == ' ':
                x.append(j)
            elif j.isupper():
                j = j.lower()
                x.append(j)
            else:
                j = j.upper()
                x.append(j)
    print(x)
    return ''.join(x)
