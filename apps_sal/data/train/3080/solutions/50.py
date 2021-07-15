def who_is_paying(name):
    b = []
    if len(name) <= 2:
        b.append(name)
        return b
    else:
        b.append(name)
        b.append(name[:2])
    return b
