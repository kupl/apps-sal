def oper(fct, s):
    return fct(s)


def vert_mirror(strng):
    vert = strng.split()
    vert1 = []
    vert2 = '\n'
    for i in range(len(vert)):
        vert1.append(vert[i][::-1])
    return (vert2.join(vert1))


def hor_mirror(strng):
    hor = strng.split()
    hor1 = hor[::-1]
    hor2 = '\n'
    return hor2.join(hor1)
