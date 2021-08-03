def no_space(x):
    kk = ''
    for i in x:
        if i == " ":
            continue
        else:
            kk = kk + i
    return kk
