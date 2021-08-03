def distinct(seq):
    ls = []
    for i in seq:
        if i in ls:
            continue
        ls.append(i)
    return ls
