def triple_trouble(one, two, three):
    s = ''
    a = 0
    b = [one, two, three]
    for j in one:
        for i in b:
            s += i[a]
        a += 1
    return s
