def sort_my_string(s):
    l = list(s)
    return ''.join(l[::2] + [' '] + l[1::2])
