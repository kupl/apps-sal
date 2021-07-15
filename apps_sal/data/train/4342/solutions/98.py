def no_space(x):
    z = ""
    for y in x:
        if y != " ":
            z = z + y
        else:
            pass
    return z
