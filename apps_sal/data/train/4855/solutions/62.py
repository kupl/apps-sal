def vert_mirror(strng):
    sub_list = strng.split("\n")
    for index, substr in enumerate(sub_list):
        sub_list[index] = substr[::-1]
    return "\n".join(sub_list)


def hor_mirror(strng):
    sub_list = strng.split("\n")
    sub_list.reverse()
    return "\n".join(sub_list)


def oper(fct, s):
    return fct(s)
