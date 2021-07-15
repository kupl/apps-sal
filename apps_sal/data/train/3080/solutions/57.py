def who_is_paying(name):
    if len(name) == 0:
        return [""]
    if len(name) <= 2:
        return name.split()
    alist = []
    alist.extend([name, name[0:2]])
    print(alist)
    return alist
