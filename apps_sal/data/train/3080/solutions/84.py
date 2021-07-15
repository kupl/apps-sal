def who_is_paying(name):
    if len(name) > 2:
        trunc_name = name[0:2]
        output = [name, trunc_name]
    else:
        output = [name]
    return output

