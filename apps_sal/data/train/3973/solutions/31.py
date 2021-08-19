def remove_char(s):
    s1 = []
    for x in s:
        s1.append(x)
    s1.pop(0)
    s1.pop(-1)
    s2 = ''
    for x in s1:
        s2 += x
    return s2
