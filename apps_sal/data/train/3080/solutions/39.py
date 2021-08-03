def who_is_paying(name):
    res = [name]
    if len(name) > 2:
        res.append(name[0] + name[1])
    return res
