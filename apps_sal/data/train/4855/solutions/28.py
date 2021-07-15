def vert_mirror(strng):
    strng = strng.split("\n")
    res = []
    for substr in strng:
        res.append(substr[::-1])
    res = '\n'.join(res)
    return res
def hor_mirror(strng):
    strng = strng.split("\n")
    res = []
    for index in range(len(strng)):
        res.append(strng[len(strng) - index - 1])
    res = '\n'.join(res)
    return res
def oper(fct, s):
    if (fct == vert_mirror):
        return vert_mirror(s)
    elif (fct == hor_mirror):
        return hor_mirror(s)

