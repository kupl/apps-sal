def who_is_paying(name):
    if name == '':
        return ['']
    elif len(name) == 1:
        return [name]
    elif len(name) == 2:
        return [name]
    else:
        return [name, name[:2]]
