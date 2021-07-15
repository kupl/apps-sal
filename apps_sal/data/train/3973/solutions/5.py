def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)
