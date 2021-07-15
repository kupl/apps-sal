def who_is_paying(name):
    namelist = []
    namelist.append(name)
    if len(name) <= 2:
        return namelist
    if len(name) > 2:
        namelist.append(name[:2])
        return namelist
