def who_is_paying(name):
    if len(name) == 1 or len(name) == 2:
        return [name]
    list = [name]
    if len(name) > 1:
        list.append(name[0]+name[1])
    elif len(name) > 0:
        list.append(name[0])
    return list
