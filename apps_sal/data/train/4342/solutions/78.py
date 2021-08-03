def no_space(x):
    x = list(x)
    l = ''
    for i in x:
        if i != " ":
            l = l + i
    return l
