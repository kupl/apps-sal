def who_is_paying(name):
    if len(name) >= 3:
        return [name, name[0] + name[1]]
    if len(name) <= 2:
        return [name]
    else:
        return ['']
