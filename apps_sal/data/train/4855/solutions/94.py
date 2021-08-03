def vert_mirror(s):
    return '\n'.join(_[::-1] for _ in s.split())


def hor_mirror(s):
    return '\n'.join(s.split()[::-1])


def oper(fct, s):
    return fct(s)
# Flez
