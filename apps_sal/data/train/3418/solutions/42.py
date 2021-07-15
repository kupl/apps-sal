def reverse_list(l):
    c = []
    for x in l[::-1]:
        if x != None:
            c.append(x)
    return c
