def poly_subtract(p1, p2):
    p1length = len(p1)
    p2length = len(p2)
    length = max(p1length, p2length)
    list = []
    for i in range(0, length):
        a = 0
        b = 0
        if i < p1length:
            a = p1[i]
        if i < p2length:
            b = p2[i]
        list.append(a - b)
    print(list)
    return list
