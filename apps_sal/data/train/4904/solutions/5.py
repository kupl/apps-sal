def unpack(li,s=None):
    if s is None : s = []
    for i in li:
        if type(i) in [list, tuple, set] : unpack(i,s)
        elif type(i) == dict : unpack(sum([[k, l] for k, l in i.items()], []),s)
        else : s.append(i)
    return s
