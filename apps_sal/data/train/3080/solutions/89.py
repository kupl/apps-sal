def who_is_paying(name):
    if len(name) > 2:
        return list((name, name[:2]))
    else:
        return [name]
