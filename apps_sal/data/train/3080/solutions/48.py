def who_is_paying(name):
    if len(name) < 3:
        return [name]
    else:
        first_two = name[0:2]
        return [name, first_two]
