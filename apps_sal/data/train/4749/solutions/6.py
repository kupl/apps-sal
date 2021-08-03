def base_finder(seq):
    a = []
    b = []
    for i in seq:
        for j in i:
            a.append(j)
    for digit in a:
        if digit not in b:
            b.append(digit)
    return len(b)
