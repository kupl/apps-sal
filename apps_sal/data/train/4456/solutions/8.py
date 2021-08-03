def flatten_me(lst):
    out = []
    for item in lst:
        if type(item) is list:
            out += (x for x in item)
        else:
            out.append(item)
    return out
