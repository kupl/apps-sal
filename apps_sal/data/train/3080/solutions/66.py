def who_is_paying(name):
    m = []
    if len(name) <= 2:
        m.append(name)
        return m
    g = [name, name[:2]]
    return g
