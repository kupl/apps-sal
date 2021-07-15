def who_is_paying(name):
    r = [name]
    if len(name) > 2:
        r = [name, name[:2]]
    return r
