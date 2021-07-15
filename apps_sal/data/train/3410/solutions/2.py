def scratch(l):
    c = 0
    for i in l:
        i = i.split()
        if i[0] == i[1] == i[2]:
            c += int(i[3])
    return c
