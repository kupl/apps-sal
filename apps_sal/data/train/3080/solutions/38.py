def who_is_paying(name):
    a = []
    i = 0
    for item in name:
        i += 1
    if i > 2:
        a.append(name)
        a.append(name[0] + name[1])
    else:
        a.append(name)
    return a
