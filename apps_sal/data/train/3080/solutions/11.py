def who_is_paying(name):
    return [[name], [name, name[:2]]][len(name) > 2]
