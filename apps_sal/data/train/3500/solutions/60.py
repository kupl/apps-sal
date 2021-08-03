def remove_exclamation_marks(s):
    m = list(s)
    x = []
    for i in m:
        if i != "!":
            x.append(i)
    v = "".join(x)
    return v
