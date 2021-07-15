def who_is_paying(name):
    list = [name]
    if len(name) > 2:
        list.append(name[0:2])
        return list
    else:
        return list
