def vert_mirror(strng):
    segments = strng.split('\n')
    for i in range(len(segments)):
        segments[i] = segments[i][::-1]
    return segments


def hor_mirror(strng):
    segments = strng.split('\n')
    s = segments[::-1]
    return s


def oper(fct, s):
    return '\n'.join(fct(s))
