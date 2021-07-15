def who_is_paying(name):
    if len(name) > 2:
        names = [name,name[:2]]
        return names
    else:
        return [name]
