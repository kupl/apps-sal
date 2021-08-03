def who_is_paying(name):
    listsx = [name, ''.join(list(name)[:2])] if len(name) > 2 else [name]
    return listsx
