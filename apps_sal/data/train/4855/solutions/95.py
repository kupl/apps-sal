def vert_mirror(s):
    s = s.splitlines()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    s = '\n'.join(s)
    return s

def hor_mirror(s):
    s = s[::-1].splitlines()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    s = '\n'.join(s)
    return s

def oper(fct, s):
    return fct(s)
