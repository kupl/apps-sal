def vert_mirror(strng):
    return '\n'.join((i[::-1] for i in strng.split('\n')))


def hor_mirror(strng):
    return '\n'.join((''.join(i) for i in [(c for c in word) for word in strng.split('\n')][::-1]))


def oper(fct, s):
    return fct(s)
