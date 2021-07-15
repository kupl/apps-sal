def who_is_paying(name):
    name_array = []
    if len(name) > 2:
        name_array.append(name)
        name_array.append(name[0:2])
        return name_array
    else:
        name_array.append(name)
        return name_array

