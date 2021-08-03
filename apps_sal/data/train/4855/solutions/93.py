def vert_mirror(s):
    splitted_s = s.split('\n')
    l = []
    for word in splitted_s:
        reversed_word = word[::-1]
        l.append(reversed_word)
    new_s = '\n'.join(l)
    return(new_s)


def hor_mirror(s):
    splitted_s = s.split('\n')
    splitted_s.reverse()
    return('\n'.join(splitted_s))


def oper(fct, s):
    return(fct(s))
