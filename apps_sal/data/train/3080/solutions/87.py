def who_is_paying(name):
    if name == '':
        return ['']
    elif name == 'I':
        return ['I']
    elif name == name[0:2]:
        return [name]
    else:
        return [name, name[0:2]]
