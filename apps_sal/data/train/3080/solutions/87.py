def who_is_paying(name):
    if name == '':
        return ['']
    elif name == 'I':
        return ['I']
    else:
        if name == name[0:2]:
            return [name]
        else:
            return [name, name[0:2]]
