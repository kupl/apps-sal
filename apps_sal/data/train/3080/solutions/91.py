def who_is_paying(name):
    if len(name) <= 2:
        return ([name])

    else:
        name_list = list(name)
        name_2 = name_list[0:2]
        name_str = ''.join(name_2)
        return ([name, name_str])


