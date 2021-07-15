def symmetric_point(p, q):
    arr = []
    for i in zip(p, q):
        x = i[1] - i[0]
        arr.append(i[1] + x)
    return arr    

