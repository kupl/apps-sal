def no_space(x):
    x = list(x)
    y = ""
    for k in x:
        if k != " ":
            y += k
    return y
