def compound_array(a, b):
    if a == [] or b == []:
        return a + b
    n = []
    for x in range(len(min([a, b], key=len))):
        n.append(a[x])
        n.append(b[x])
        if x == len(min([a, b], key=len)) - 1:
            n += max([a, b], key=len)[x + 1:]
    return n
