def who_is_paying(name):
    if name == name[0:2]:
        return [name]
    else:
        return [name, name[0:2]]
