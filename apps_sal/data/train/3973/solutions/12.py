def remove_char(s):
    list_s = list(s)
    list_s.pop()
    list_s.pop(0)
    return ''.join(list_s)
