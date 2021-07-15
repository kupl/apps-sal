def who_is_paying(name):
    names= []
    if len(name) > 2:
        names.append(name)
        names.append(name[0:2])
    else:
        names.append(name)
    return names
