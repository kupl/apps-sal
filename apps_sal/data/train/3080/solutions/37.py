def who_is_paying(name):
    if len(name) > 2:
        short = name[0:2]
        val = []
        val.append(name)
        val.append(short)
        return val
    elif len(name) <= 2:
        val = []
        val.append(name)
        return val
    else:
        return None
