def reverse_list(l):
    c = -1
    d = []
    for i in l:
        d.append(l[c])
        c -= 1
    return d
