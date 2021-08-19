def vert_mirror(strng):
    strng = strng.split('\n')
    output = []
    for word in strng:
        output.append(word[::-1])
    return '\n'.join(output)


def hor_mirror(strng):
    strng = strng.split('\n')
    output = []
    return '\n'.join(strng[::-1])


def oper(fct, s):
    return fct(s)
