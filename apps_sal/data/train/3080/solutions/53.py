def who_is_paying(name):
    if len(name) == 1:
        return [name]
    elif name == '':
        return ['']
    elif name == name[0:2]:
        return [name]
    else:
        return [name,name[0:2]]
