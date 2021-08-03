def vert_mirror(s):
    return '\n'.join([s.split('\n')[0][::-1]] + [m[1:][::-1] + m[0] for m in s.split('\n')[1:]])


def hor_mirror(s):
    return '\n'.join(s.split('\n')[::-1])


def oper(fct, s):
    return fct(s)
