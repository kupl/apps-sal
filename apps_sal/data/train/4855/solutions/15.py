def vert_mirror(lines):
    return '\n'.join(line[::-1] for line in lines.split('\n'))
def hor_mirror(lines):
    return '\n'.join(lines.split('\n')[::-1])
def oper(fct, s):
    return fct(s)
