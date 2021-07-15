def code(x, y):
    list = []
    for n in [x,y]:
        list.append(int('9' * len(str(n))) - n)
    return sum(list)
