def remove_char(s):
    l = list(s)
    nl = [j for i,j in enumerate(l) if i != 0 and i != len(s)-1]
    return ''.join(nl)
