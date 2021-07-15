def who_is_paying(name):
    name_list = []
    if len(name) <= 2:
        name_list.append(name[0:2])
    elif len(name) == 0:
        name_list.append("")
    elif len(name) > 2:
        name_list.append(name)
        name_list.append(name[0:2])
    return name_list
