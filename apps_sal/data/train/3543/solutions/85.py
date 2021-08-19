def increment_string(strng):
    s = ''
    a = ''
    for i in strng[::-1]:
        if i.isnumeric() and len(a) == 0:
            s += i
        else:
            a += i
    if len(s) == 0:
        return strng + '1'
    a = a[::-1]
    s = s[::-1]
    s2 = int(s) + 1
    return a + str(s2).zfill(len(s))
