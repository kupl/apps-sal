def who_is_paying(name):
    if len(name) == 0:
        return [""]
    elif len(name) < 3:
        return [name]
    else:
        return [name, name[:2]]
