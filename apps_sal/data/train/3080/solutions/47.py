def who_is_paying(name):
    if len(name) <= 2:
        who = [name]
    else:
        who = [name, name[0:2]]
    return who
