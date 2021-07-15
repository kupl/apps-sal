def who_is_paying(name):
    if len(name) <=2:
        result = [name]
    else:
        result = [name,name[0:2]]
    return result
