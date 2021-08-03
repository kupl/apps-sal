def capitalize(s, ind):
    return "".join(x.upper() if i in ind else x for i, x in enumerate(s))
