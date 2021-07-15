def accum(s):
    return "-".join(list(x.upper() + x.lower() * count for count, x in enumerate(s)))
