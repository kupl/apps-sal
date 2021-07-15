def who_is_paying(name):
    if name[:2] == name:
        return [name]
    else:
        return [name, name[:2]]
