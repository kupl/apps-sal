def who_is_paying(name):
    if len(name) == 0:
        return ['']
    elif len(name) == 1:
        return [name[0]]
    elif len(name) == 2:
        return [name[0] + name[1]]
    else:
        return [name, name[0] + name[1]]
