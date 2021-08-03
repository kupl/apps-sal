def vert_mirror(strng):
    lst_string = strng.split('\n')
    i = 0
    while i < len(lst_string):
        lst_string[i] = lst_string[i][::-1]
        i += 1
    return '\n'.join(lst_string)


def hor_mirror(strng):
    lst_string = strng.split('\n')
    i = 0
    l = len(lst_string)
    while i < l // 2:
        fst_s = lst_string[i]
        lst_string[i] = lst_string[l - 1 - i]
        lst_string[l - 1 - i] = fst_s
        i += 1
    return '\n'.join(lst_string)


def oper(fct, s):
    return fct(s)
