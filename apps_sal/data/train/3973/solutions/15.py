def remove_char(s):
    a = list(s)
    a.pop()
    a.reverse()
    a.pop()
    a.reverse()
    return ''.join(a)
