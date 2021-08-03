def who_is_paying(name):
    if len(name) <= 2:
        char_list = [name]
        return char_list
    else:
        name_list = [name, name[:2]]
        return name_list
