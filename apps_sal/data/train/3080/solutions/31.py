def who_is_paying(name):
    oplst = [name]
    if len(name) <= 2:
        return oplst
    else:
        oplst.append(name[:2])
        return oplst
