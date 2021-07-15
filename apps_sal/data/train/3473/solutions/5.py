def doubles(s):
    for _ in range(9):
        for i in set(s):
            s = s.replace(i+i, '')
    return s
