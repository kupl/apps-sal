def who_is_paying(name):
    d = [name]
    if len(name)<3:
        return d
    else:
        d.append(name[0:2])
        return d
