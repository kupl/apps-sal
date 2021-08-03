def who_is_paying(name):
    out = []
    if len(name) > 2:
        out.append(name)
        out.append(name[0:2])
    else:
        out.append(name)
    return out
