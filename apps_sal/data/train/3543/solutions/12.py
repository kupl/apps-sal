import string


def increment_string(strng):
    if strng == '':
        return '1'
    a = list(strng)
    s = ''
    for i in range(0, len(a)):
        if a[-1] in string.digits:
            s += a[-1]
            del a[-1]
    s = reversed(s)
    s = ''.join(s)
    if s == '':
        s = '0'
    c = len(s)
    aa = int(s)
    aa += 1
    a = ''.join(a)
    return str(a) + str(aa).zfill(c)
