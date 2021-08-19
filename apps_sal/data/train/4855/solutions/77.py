def vert_mirror(strng):
    arr = [s[::-1] for s in strng.split('\n')]
    return '\n'.join(arr)


def hor_mirror(strng):
    print('there')
    return '\n'.join([s for s in strng.split('\n')][::-1])


def oper(fct, s):
    return fct(s)
