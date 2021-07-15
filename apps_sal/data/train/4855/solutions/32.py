def vert_mirror(strng):
    return (line[::-1] for line in strng.split('\n'))
def hor_mirror(strng):
    return strng.split('\n')[::-1]
    # your code
def oper(fct, s):
    return '\n'.join(fct(s))
