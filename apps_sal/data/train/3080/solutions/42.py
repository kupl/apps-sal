def who_is_paying(name):
    sliced = name[0:2]
    if (sliced == name):
        return [sliced]
    return [name, sliced]
