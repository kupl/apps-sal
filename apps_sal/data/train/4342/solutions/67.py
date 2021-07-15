def no_space(x):
    z = ""
    for i in x:
        if not i == " ":
            z = z + i
    return z
