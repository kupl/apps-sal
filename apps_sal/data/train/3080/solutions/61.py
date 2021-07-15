def who_is_paying(name):
    x = []
    y = []
    if len(name) <= 2:
        x.append(name)
    else:
        x.append(name)
        y.append(name[0])
        y.append(name[1])
        z = ''.join(map(str, y))
        x.append(z)
    return x

