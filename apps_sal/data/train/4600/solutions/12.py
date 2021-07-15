def move_zeros(array):
    a = []
    b = []
    for v in array:
        if type(v) in [float, int] and v == 0:
            b.append(0)
        else:
            a.append(v)
    return a+b
