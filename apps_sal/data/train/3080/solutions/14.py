def who_is_paying(name):
    return [name, name[0] + name[1]] if len(name) > 2 else [name]
